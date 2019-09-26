from ..client import InvalidJSONError
from ..client import ResponseStructureError
from .base import Base

DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

MINUTES_IN_HOUR = 60


class Subscription(Base):
    def __init__(self, client, tags, contacts=None, enabled=None, throttling=None, sched=None,
                 ignore_warnings=False, ignore_recoverings=False, plotting=None, any_tags=False, **kwargs):
        """

        :param client: api client
        :param tags: list of str tags
        :param contacts: list of contact id's
        :param enabled: bool is enabled
        :param throttling: bool throttling
        :param sched: dict schedule
        :param ignore_warnings: bool ignore warnings
        :param ignore_recoverings: bool ignore recoverings
        :param plotting: dict plotting settings
        :param any_tags: bool any tags
        :param kwargs: additional parameters
        """
        self._client = client

        self._id = kwargs.get('id', None)
        self.tags = tags if not any_tags else []
        if not contacts:
            contacts = []
        self.contacts = contacts
        self.enabled = enabled
        self.any_tags = any_tags
        self.throttling = throttling
        default_sched = {
            'startOffset': 0,
            'endOffset': 1439,
            'tzOffset': 0
        }
        if not sched:
            sched = default_sched
            self.disabled_days = set()
        else:
            if 'days' in sched and sched['days'] is not None:
                self.disabled_days = {day['name'] for day in sched['days'] if not day['enabled']}
        self.sched = sched

        # compute time range
        self._start_hour = self.sched['startOffset'] // MINUTES_IN_HOUR
        self._start_minute = self.sched['startOffset'] - self._start_hour * MINUTES_IN_HOUR
        self._end_hour = self.sched['endOffset'] // MINUTES_IN_HOUR
        self._end_minute = self.sched['endOffset'] - self._end_hour * MINUTES_IN_HOUR

        self.ignore_warnings = ignore_warnings
        self.ignore_recoverings = ignore_recoverings

        if not plotting:
            plotting = {'enabled': False, 'theme': 'light'}
        self.plotting = plotting

    def _send_request(self, subscription_id=None):
        data = {
            'contacts': self.contacts,
            'tags': self.tags,
            'enabled': self.enabled,
            'throttling': self.throttling,
            'sched': self.sched,
            'ignore_warnings': self.ignore_warnings,
            'ignore_recoverings': self.ignore_recoverings,
            'plotting': self.plotting
        }

        if subscription_id:
            data['id'] = subscription_id

        data['sched']['days'] = []
        for day in DAYS_OF_WEEK:
            day_info = {
                'enabled': True if day not in self.disabled_days else False,
                'name': day
            }
            data['sched']['days'].append(day_info)

        data['sched']['startOffset'] = self._start_hour * MINUTES_IN_HOUR + self._start_minute
        data['sched']['endOffset'] = self._end_hour * MINUTES_IN_HOUR + self._end_minute

        if subscription_id:
            result = self._client.put('subscription/' + subscription_id, json=data)
        else:
            result = self._client.put('subscription', json=data)
        if 'id' not in result:
            raise ResponseStructureError("id doesn't exist in response", result)

        self._id = result['id']
        return self._id

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

    def add_tag(self, tag):
        """
        Add tag to subscription

        :param tag: str tag name
        :return: None
        """
        self.tags.append(tag)

    def add_contact(self, contact_id):
        """
        Add contact

        :param contact_id: str contact id
        :return: None
        """
        self.contacts.append(contact_id)

    def enable_plotting(self, theme='light'):
        """
        Enable plotting

        :param theme: str plotting theme
        :return: None
        """
        self.plotting = {
            'enabled': True,
            'theme': theme
            }

    def disable_plotting(self):
        """
        Disable plotting

        :return: None
        """
        self.plotting = {
            'enabled': False,
            'theme': 'light'
            }

    def save(self):
        """
        Save subscription

        :return: subscription id
        """
        if self._id:
            return self.update()
        self._send_request()

    def update(self):
        """
        Update subscription

        :return: subscription id
        """
        if not self._id:
            return self.save()
        self._send_request(self._id)

    def set_start_hour(self, hour):
        """
        Set start hour

        :param hour: int hour

        :return: None
        """
        self._start_hour = hour

    def set_start_minute(self, minute):
        """
        Set start minute

        :param minute: int minute

        :return: None
        """
        self._start_minute = minute

    def set_end_hour(self, hour):
        """
        Set end hour

        :param hour: int hour

        :return: None
        """
        self._end_hour = hour

    def set_end_minute(self, minute):
        """
        Set end minute

        :param minute: int minute

        :return: None
        """
        self._end_minute = minute


class SubscriptionManager:
    def __init__(self, client):
        self._client = client

    def fetch_all(self):
        """
        Returns all existing subscriptions

        :return: list of Subscription

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())
        if 'list' in result:
            subscriptions = []
            for subscription in result['list']:
                subscriptions.append(Subscription(self._client, **subscription))
            return subscriptions
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def is_exist(self, **kwargs):
        """
        Check whether subscription exists or not by any attributes

        :param kwargs: attributes
        :return: bool

        :raises: ValueError
        """
        for subscription in self.fetch_all():
            equal = True
            for attr, value in kwargs.items():
                try:
                    if getattr(subscription, attr) != value:
                        equal = False
                        break
                except Exception:
                    raise ValueError('Wrong attibute "{}"'.format(attr))
            if equal:
                return True
        return False

    def create(self, tags, contacts=None, enabled=True, throttling=True, sched=None,
               ignore_warnings=False, ignore_recoverings=False, plotting=None, any_tags=False, **kwargs):
        """
        Create new subscription.
        
        :param tags: list of str tags
        :param contacts: list of contact id's
        :param enabled: bool is enabled
        :param throttling: bool throttling
        :param sched: dict schedule
        :param ignore_warnings: bool ignore warnings
        :param ignore_recoverings: bool ignore recoverings
        :param kwargs: additional parameters
        :param plotting: dict plotting settings
        :param any_tags: bool any tags
        :return: Subscription
        """

        return Subscription(
            self._client,
            tags,
            contacts, 
            enabled,
            throttling,
            sched,
            ignore_warnings,
            ignore_recoverings,
            plotting,
            any_tags,
            **kwargs
        )

    def delete(self, subscription_id):
        """
        Remove subscription by given id

        :return: True on success, False otherwise
        """
        try:
            self._client.delete(self._full_path(subscription_id))
            return False
        except InvalidJSONError as e:
            if e.content == b'':  # successfully if response is blank
                return True
            return False

    def test(self, subscription_id):
        """
        Send test notification to subscription contact

        :return: True on success, False otherwise
        """
        try:
            self._client.put(self._full_path(subscription_id) + "/test")
            return False
        except InvalidJSONError as e:
            if e.content == b'':  # successfully if response is blank
                return True
            return False

    def _full_path(self, path=''):
        if path:
            return 'subscription/' + path
        return 'subscription'
