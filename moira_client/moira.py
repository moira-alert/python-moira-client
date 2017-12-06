from .client import Client
from .models.contact import ContactManager
from .models.event import EventManager
from .models.notification import NotificationManager
from .models.pattern import PatternManager
from .models.subscription import SubscriptionManager
from .models.tag import TagManager
from .models.trigger import TriggerManager


class Moira:
    def __init__(self, api_url, auth_custom=None,
                 auth_user=None, auth_pass=None, login=None):
        """
        :param api_url: str API URL
        :param auth_custom: dict auth custom headers
        :param auth_user: str auth user
        :param auth_pass: str auth password
        :param login: str auth login
        """
        self._client = Client(api_url, auth_custom,
                              auth_user, auth_pass, login)

        self._trigger = None
        self._tag = None
        self._event = None
        self._notification = None
        self._contact = None
        self._pattern = None
        self._subscription = None

    @property
    def trigger(self):
        """
        Get trigger manager

        :return: TriggerManager
        """
        if not self._trigger:
            self._trigger = TriggerManager(self._client)
        return self._trigger

    @property
    def tag(self):
        """
        Get tag manager

        :return: TagManager
        """
        if not self._tag:
            self._tag = TagManager(self._client)
        return self._tag

    @property
    def event(self):
        """
        Get event manager

        :return: EventManager
        """
        if not self._event:
            self._event = EventManager(self._client)
        return self._event

    @property
    def notification(self):
        """
        Get notification manager

        :return: NotificationManager
        """
        if not self._notification:
            self._notification = NotificationManager(self._client)
        return self._notification

    @property
    def contact(self):
        """
        Get contact manager

        :return: ContactManager
        """
        if not self._contact:
            self._contact = ContactManager(self._client)
        return self._contact

    @property
    def pattern(self):
        """
        Get pattern manager

        :return: PatternManager
        """
        if not self._pattern:
            self._pattern = PatternManager(self._client)
        return self._pattern

    @property
    def subscription(self):
        """
        Get subscription manager

        :return: SubscriptionManager
        """
        if not self._subscription:
            self._subscription = SubscriptionManager(self._client)
        return self._subscription
