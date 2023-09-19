from ..client import ResponseStructureError
from ..client import InvalidJSONError
from .base import Base

STATE_OK = 'OK'
STATE_WARN = 'WARN'
STATE_ERROR = 'ERROR'
STATE_NODATA = 'NODATA'
STATE_EXCEPTION = 'EXCEPTION'

RISING_TRIGGER = 'rising'
FALLING_TRIGGER = 'falling'
EXPRESSION_TRIGGER = 'expression'

GRAPHITE_LOCAL = 'graphite_local'
GRAPHITE_REMOTE = 'graphite_remote'
PROMETHEUS_REMOTE = 'prometheus_remote'

class Trigger(Base):
    QUERY_PARAM_VALIDATE_FLAG = 'validate'

    def __init__(
            self,
            client,
            name,
            tags,
            targets,
            warn_value=None,
            error_value=None,
            desc='',
            ttl=600,
            ttl_state=STATE_NODATA,
            sched=None,
            expression='',
            trigger_type=None,
            is_remote=False,
            mute_new_metrics=False,
            alone_metrics=None,
            trigger_source=None,
            **kwargs):
        """

        :param client: api client
        :param name: str trigger name
        :param tags: list of str tags for trigger
        :param targets: list of str targets
        :param warn_value: float warning value (if T1 <= warn_value)
        :param error_value: float error value (if T1 <= error_value)
        :param desc: str trigger description
        :param ttl: int set ttl_state if has no value for ttl seconds
        :param ttl_state: str state after ttl seconds without data (one of STATE_* constants)
        :param sched: dict schedule for trigger
        :param expression: str c-like expression
        :param trigger_type: str trigger type
        :param is_remote: bool use remote storage
        :param mute_new_metrics: bool mute new metrics
        :param alone_metrics: dict with targets of alone metrics
        :param kwargs: additional parameters
        :param trigger_source: str specify trigger source, overrides is_remote 
        """
        self._client = client

        self._id = kwargs.get('id', None)
        self.name = name
        self.tags = tags
        self.targets = targets
        self.warn_value = warn_value
        self.error_value = error_value
        self.desc = desc
        self.ttl = ttl
        self.ttl_state = ttl_state
        self.sched = sched
        self.expression = expression
        self.trigger_type = self.resolve_type(trigger_type)

        self.is_remote = is_remote
        self.trigger_source = trigger_source
        self.mute_new_metrics = mute_new_metrics
        self.alone_metrics = alone_metrics

    def resolve_type(self, trigger_type):
        """
        Resolve type of a trigger
        :return: str
        """
        if trigger_type in (RISING_TRIGGER, FALLING_TRIGGER, EXPRESSION_TRIGGER):
            return trigger_type
        if self.expression != '':
            return EXPRESSION_TRIGGER
        if self.warn_value is not None and self.error_value is not None:
            if self.warn_value > self.error_value:
                return FALLING_TRIGGER
            if self.warn_value < self.error_value:
                return RISING_TRIGGER

    def add_target(self, target):
        """
        Add pattern name

        :param target: str target pattern
        :return: None
        """
        self.targets.append(target)

    def add_tag(self, tag):
        """
        Add tag to trigger

        :param tag: str tag name
        :return: None
        """
        self.tags.append(tag)

    def disable_day(self, day):
        """
        Disable day

        :param day: str one of DAYS_OF_WEEK
        :return: None
        """
        self.disabled_days.add(day)

    def enable_day(self, day):
        """
        Enable day

        :param day: str one of DAYS_OF_WEEK
        :return: None
        """
        self.disabled_days.remove(day)

    @property
    def id(self):
        return self._id

    def _send_request(self, trigger_id=None):
        data = {
            'name': self.name,
            'tags': self.tags,
            'targets': self.targets,
            'warn_value': self.warn_value,
            'error_value': self.error_value,
            'desc': self.desc,
            'ttl': self.ttl,
            'ttl_state': self.ttl_state,
            'sched': self.sched,
            'expression': self.expression,
            'is_remote': self.is_remote,
            'trigger_type': self.trigger_type,
            'mute_new_metrics': self.mute_new_metrics,
            'alone_metrics': self.alone_metrics,
        }

        if self.trigger_source:
            data['trigger_source'] = self.trigger_source

        if trigger_id:
            data['id'] = trigger_id
            api_response = TriggerManager(self._client).fetch_by_id(trigger_id)

        if trigger_id and api_response:
            res = self._client.put('trigger/{}?{}'.format(trigger_id, self.QUERY_PARAM_VALIDATE_FLAG), json=data)
        else:
            res = self._client.put('trigger?{}'.format(self.QUERY_PARAM_VALIDATE_FLAG), json=data)

        if 'id' not in res:
            raise ResponseStructureError('id not in response', res)

        self._id = res['id']
        return res

    def save(self):
        """
        Save trigger

        :return: response object
        """
        if self._id:
            return self.update()
        trigger = self.check_exists()

        if trigger:
            self._id = trigger.id
            return self.update()

        return self._send_request()

    def update(self):
        """
        Update trigger

        :return: response object
        """
        return self._send_request(self._id)

    def set_start_hour(self, hour):
        """
        Set start hour

        :param hour: int hour
        :return: None
        """
        self._start_hour = int(hour)

    def set_start_minute(self, minute):
        """
        Set start minute

        :param minute: int minute
        :return: None
        """
        self._start_minute = int(minute)

    def set_end_hour(self, hour):
        """
        Set end hour

        :param hour: int hour
        :return: None
        """
        self._end_hour = int(hour)

    def set_end_minute(self, minute):
        """
        Set end minute

        :param minute: int minute
        :return: None
        """
        self._end_minute = int(minute)

    def check_exists(self):
        """
        Check if current trigger exists

        :return: trigger id if exists, None otherwise
        """
        trigger_manager = TriggerManager(self._client)
        for trigger in trigger_manager.fetch_all():
            if self.name == trigger.name and \
                    set(self.targets) == set(trigger.targets) and \
                    set(self.tags) == set(trigger.tags):
                return trigger

    def get_metrics(self, start, end):
        """
        Get metrics associated with certain trigger

        :param start: The start period of metrics to get. Example : -1hour
        :param end: The end period of metrics to get. Example : now

        :return: Metrics for trigger
        """
        try:
            params = {
                'from': start,
                'to': end,
            }
            result = self._client.get('trigger/{id}/metrics'.format(id=self.id), params=params)
            return result
        except InvalidJSONError:
            return []

    def delete_metric(self, metric_name):
        """
        Deletes metric from last check and all trigger pattern metrics

        :param metric_name: str name of the target metric, example: DevOps.my_server.hdd.freespace_mbytes

        :return: True if success, False otherwise
        """
        try:
            params = {
                'name': metric_name,
            }
            self._client.delete('trigger/{id}/metrics'.format(id=self.id), params=params)
            return True
        except InvalidJSONError:
            return False

    def delete_nodata_metrics(self):
        """
        Deletes all metrics from last data which are in NODATA state.
        It also deletes all trigger patterns of those metrics.

        :return: True if success, False otherwise
        """
        try:
            self._client.delete('trigger/{id}/metrics/nodata'.format(id=self.id))
            return True
        except InvalidJSONError:
            return False


class TriggerManager:
    def __init__(self, client):
        self._client = client

    @property
    def trigger_client(self):
        return self._client

    def fetch_all(self):
        """
        Returns all existing triggers

        :return: list of Trigger

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())
        if 'list' in result:
            triggers = []
            for trigger in result['list']:
                triggers.append(Trigger(self._client, **trigger))
            return triggers
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def fetch_by_id(self, trigger_id):
        """
        Returns Trigger by trigger id

        :param trigger_id: str trigger id
        :return: Trigger

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path('{id}/state'.format(id=trigger_id)))
        if 'state' in result:
            trigger = self._client.get(self._full_path(trigger_id))
            return Trigger(self._client, **trigger)
        elif not 'trigger_id' in result:
            raise ResponseStructureError("invalid api response", result)

    def search(self, only_problems, page, text):
        """
        Search triggers

        :param only_problems: Restricts the result to errors only. Example: false
        :param page: Defines the number of the displayed page. E.g, page=2 would display the 2nd page. Example: 1
        :param text: Query to perform a search for. Example: cpu

        :return: matching triggers list

        :raises: ResponseStructureError
        """
        params = {
            'onlyProblems': only_problems,
            'page': page,
            'text': text,
        }
        result = self._client.get(self._full_path(), params=params)
        if 'list' not in result:
            raise ResponseStructureError("list doesn't exist in response", result)

        return result['list']

    def delete(self, trigger_id):
        """
        Delete trigger by trigger id

        :param trigger_id: str trigger id
        :return: True if deleted, False otherwise
        """
        try:
            self._client.delete(self._full_path(trigger_id))
            return False
        except InvalidJSONError:
            return True

    def get_throttling(self, trigger_id):
        """
        Get a trigger with its throttling i.e its next allowed message time

        :param trigger_id: str trigger id
        :return: trigger throttle value or None
        """
        try:
            result = self._client.get(self._full_path('{id}/throttling'.format(id=trigger_id)))
            if 'throttling' in result:
                return result['throttling']
            return None
        except InvalidJSONError:
            return None

    def reset_throttling(self, trigger_id):
        """
        Resets throttling by trigger id

        :param trigger_id: str trigger id
        :return: True if reset, False otherwise
        """
        try:
            self._client.delete(self._full_path('{id}/throttling'.format(id=trigger_id)))
            return True
        except InvalidJSONError:
            return False

    def get_state(self, trigger_id):
        """
        Get state of trigger by trigger id

        :param trigger_id: str trigger id
        :return: state of trigger
        """
        return self._client.get(self._full_path('{id}/state'.format(id=trigger_id)))

    def get_metrics(self, trigger_id, _from, to):
        """
        Get metrics associated with certain trigger

        :param trigger_id: str trigger id
        :param _from: The start period of metrics to get. Example : -1hour
        :param to: The end period of metrics to get. Example : now

        :return: Metrics for trigger
        """
        try:
            params = {
                'from': _from,
                'to': to,
            }
            result = self._client.get(self._full_path('{id}/metrics'.format(id=trigger_id)), params=params)
            return result
        except InvalidJSONError:
            return []

    def remove_metric(self, trigger_id, metric):
        """
        Remove metric by trigger id

        :param trigger_id: str trigger id
        :param metric: str metric name
        :return: True if removed, False otherwise
        """
        try:
            params = {
                'name': metric
            }
            self._client.delete(self._full_path('{id}/metrics'.format(id=trigger_id)), params=params)
            return True
        except InvalidJSONError:
            return False

    def remove_nodata_metrics(self, trigger_id):
        """
        Remove metric by trigger id

        :param trigger_id: str trigger id
        :return: True if removed, False otherwise
        """
        try:
            self._client.delete(self._full_path('{id}/metrics/nodata'.format(id=trigger_id)))
            return True
        except InvalidJSONError:
            return False

    def is_exist(self, trigger):
        """
        Check whether trigger exists or not

        :param trigger: Trigger trigger to check
        :return: bool
        """
        for moira_trigger in self.fetch_all():
            if trigger.name == moira_trigger.name and \
                    set(trigger.targets) == set(moira_trigger.targets) and \
                    set(trigger.tags) == set(moira_trigger.tags):
                return True
        return False

    def get_non_existent(self, triggers):
        """
        Returns triggers which are not exist yet

        :param triggers: list of Trigger
        :return: list of Trigger
        """
        moira_triggers = self.fetch_all()
        non_existent = []
        for trigger in triggers:
            exist = False
            for moira_trigger in moira_triggers:
                if trigger.name == moira_trigger.name and \
                        set(trigger.targets) == set(moira_trigger.targets) and \
                        set(trigger.tags) == set(moira_trigger.tags):
                    exist = True
                    break
            if not exist:
                non_existent.append(trigger)

        return non_existent

    def set_maintenance(self, trigger_id, end_time, metrics=None):
        """
        Set maintenance trigger id or metric name

        :param trigger_id: str trigger id
        :param metrics: "metric name" - "end-time" map, end-time like param end_time
        :param end_time: unix time to end the scheduled maintenance
        :return: True if success, False otherwise
        """
        try:
            data = {
                'trigger': end_time,
            }
            if metrics is not None:
                data['metrics'] = metrics
            self._client.put(self._full_path('{id}/setMaintenance'.format(id=trigger_id)), json=data)
            return True
        except InvalidJSONError:
            return False

    def create(
            self,
            name,
            tags,
            targets,
            warn_value=None,
            error_value=None,
            desc='',
            ttl=600,
            ttl_state=STATE_NODATA,
            sched=None,
            expression='',
            trigger_type=None,
            is_remote=False,
            mute_new_metrics=False,
            alone_metrics=None,
            trigger_source=None,
            **kwargs
    ):
        """
        Creates new trigger. To save it call save() method of Trigger.
        :param name: str trigger name
        :param tags: list of str tags for trigger
        :param targets: list of str targets
        :param warn_value: float warning value (if T1 <= warn_value)
        :param error_value: float error value (if T1 <= error_value)
        :param desc: str trigger description
        :param ttl: int set ttl_state if has no value for ttl seconds
        :param ttl_state: str state after ttl seconds without data (one of STATE_* constants)
        :param sched: dict schedule for trigger
        :param expression: str c-like expression
        :param trigger_type: str trigger type
        :param is_remote: bool use remote storage
        :param mute_new_metrics: bool mute new metrics
        :param alone_metrics: dict with targets of alone metrics
        :param kwargs: additional trigger params
        :param trigger_source: str specify trigger source, overrides is_remote 
        :return: Trigger
        """
        return Trigger(
            client=self._client,
            name=name,
            tags=tags,
            targets=targets,
            warn_value=warn_value,
            error_value=error_value,
            desc=desc,
            ttl=ttl,
            ttl_state=ttl_state,
            sched=sched,
            expression=expression,
            trigger_type=trigger_type,
            is_remote=is_remote,
            mute_new_metrics=mute_new_metrics,
            alone_metrics=alone_metrics,
            trigger_source=trigger_source,
            **kwargs
        )

    def _full_path(self, path=''):
        if path:
            return 'trigger/{}'.format(path)
        return 'trigger'
