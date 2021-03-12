from ..client import ResponseStructureError
from .contact import Contact
from .subscription import Subscription


class UserSettings:
    def __init__(self, login, contacts, subscriptions):
        self.login = login
        self.contacts = contacts
        self.subscriptions = subscriptions


class UserManager:
    def __init__(self, client):
        self._client = client

    def get_username(self):
        """
        Gets the username of the authenticated user if it is available.

        :return: login

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())
        if 'login' not in result:
            raise ResponseStructureError("'login' field doesn't exist in response", result)
        return result['login']

    def get_user_settings(self):
        """
        Get the user's contacts and subscriptions.

        :return: user settings

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path('settings'))
        required = ['login', 'contacts', 'subscriptions']
        for field in required:
            if field not in result:
                raise ResponseStructureError("'{}' field doesn't exist in response".format(field), result)

        contacts = []
        for contact in result['contacts']:
            contacts.append(Contact(**contact))
        result['contacts'] = contacts

        subscriptions = []
        for subscription in result['subscriptions']:
            subscriptions.append(Subscription(self._client, **subscription))
        result['subscriptions'] = subscriptions

        return UserSettings(**result)

    def _full_path(self, path=''):
        if path:
            return 'user/{}'.format(path)
        return 'user'
