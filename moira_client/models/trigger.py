from ..client import ResponseStructureError
from ..client import InvalidJSONError
from .base import Base


DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

STATE_OK = 'OK'
STATE_WARN = 'WARN'
STATE_ERROR = 'ERROR'
STATE_NODATA = 'NODATA'
STATE_EXCEPTION = 'EXCEPTION'

MINUTES_IN_HOUR = 60

RISING_TRIGGER = 'rising'
FALLING_TRIGGER = 'falling'
EXPRESSION_TRIGGER = 'expression'


class Trigger(Base):

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
        :param kwargs: additional parameters
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
        
        default_sched = {
            'startOffset': 0,
            'endOffset': 1439,
            'tzOffset': 0
        }
        if not sched:
            sched = default_sched
            self.disabled_days = set()
        else:
            if 'days' in sched:
                self.disabled_days = {day['name'] for day in sched['days'] if not day['enabled']}
        self.sched = sched
        self.expression = expression
        self.trigger_type = self.resolve_type(trigger_type)

        # compute time range
        self._start_hour = self.sched['startOffset'] // MINUTES_IN_HOUR
        self._start_minute = self.sched['startOffset'] - self._start_hour * MINUTES_IN_HOUR
        self._end_hour = self.sched['endOffset'] // MINUTES_IN_HOUR
        self._end_minute = self.sched['endOffset'] - self._end_hour * MINUTES_IN_HOUR

        self.is_remote = is_remote
        self.mute_new_metrics = mute_new_metrics

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
            'mute_new_metrics': self.mute_new_metrics
        }

        if trigger_id:
            data['id'] = trigger_id
            api_response = TriggerManager(
                self._client).fetch_by_id(trigger_id)

        data['sched']['days'] = []
        for day in DAYS_OF_WEEK:
            day_info = {
                'enabled': True if day not in self.disabled_days else False,
                'name': day
            }
            data['sched']['days'].append(day_info)

        data['sched']['startOffset'] = self._start_hour * MINUTES_IN_HOUR + self._start_minute
        data['sched']['endOffset'] = self._end_hour * MINUTES_IN_HOUR + self._end_minute

        if trigger_id and api_response:
            res = self._client.put('trigger/' + trigger_id, json=data)
        else:
            res = self._client.put('trigger', json=data)
        if 'id' not in res:
            raise ResponseStructureError('id not in response', res)
        self._id = res['id']
        return self._id

    def save(self):
        """
        Save trigger

        :return: trigger_id
        """
        if self._id:
            return self.update()
        trigger = self.check_exists()

        if trigger:
            self._id = trigger.id
            self.update()
            return trigger.id

        return self._send_request()

    def update(self):
        """
        Update trigger

        :return: trigger id
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
        result = self._client.get(self._full_path(trigger_id + '/state'))
        if 'state' in result:
            trigger = self._client.get(self._full_path(trigger_id))
            return Trigger(self._client, **trigger)
        elif not 'trigger_id' in result:
            raise ResponseStructureError("invalid api response", result)

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

    def reset_throttling(self, trigger_id):
        """
        Resets throttling by trigger id

        :param trigger_id: str trigger id
        :return: True if reset, False otherwise
        """
        try:
            self._client.delete(self._full_path(trigger_id + '/throttling'))
            return True
        except InvalidJSONError:
            return False

    def get_state(self, trigger_id):
        """
        Get state of trigger by trigger id

        :param trigger_id: str trigger id
        :return: state of trigger
        """
        return self._client.get(self._full_path(trigger_id + '/state'))

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
            self._client.delete(self._full_path(trigger_id + '/metrics'), params=params)
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
        :param kwargs: additional trigger params
        :return: Trigger
        """
        return Trigger(
            self._client,
            name,
            tags,
            targets,
            warn_value,
            error_value,
            desc,
            ttl,
            ttl_state,
            sched,
            expression,
            trigger_type,
            is_remote,
            mute_new_metrics,
            **kwargs
        )

    def _full_path(self, path=''):
        if path:
            return 'trigger/' + path
        return 'trigger'
