from collections import namedtuple

from requests.exceptions import HTTPError

from ..client import InvalidJSONError
from ..client import ResponseStructureError
from .subscription import Subscription
from .trigger import TriggerManager


TagStats = namedtuple('TagStats', ['name', 'subscriptions', 'triggers'])


class TagManager:
    def __init__(self, client):
        self._client = client

    def fetch_all(self):
        """
        Returns all existing tags

        :return: list of str

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())
        if 'list' not in result:
            raise ResponseStructureError("list doesn't exist in response", result)

        return result['list']

    def delete(self, tag):
        """
        Delete tag.
        In case if tag doesn't exist returns True.
        Returns False if tag is assigned to at least 1 trigger.

        :param tag: str tag name
        :return: True if deleted, False otherwise
        """
        try:
            self._client.delete(self._full_path(tag))
        except (InvalidJSONError, HTTPError):
            return False

        return True

    def stats(self):
        """
        Returns stats by all triggers

        :return: list of TagStats

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path('stats'))
        if 'list' in result:
            trigger_manager = TriggerManager(self._client)
            for stat in result['list']:
                if 'subscriptions' in stat:
                    stat['subscriptions'] = [
                        Subscription(self._client, **subscription) for subscription in stat['subscriptions']
                        ]
                if 'triggers' in stat:
                    stat['triggers'] = [trigger_manager.fetch_by_id(trigger_id) for trigger_id in stat['triggers']]
            return [TagStats(**stat) for stat in result['list']]
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def fetch_assigned_triggers(self, tag):
        """
        Returns triggers assigned to tag

        :param tag: str tag name
        :return: list of Trigger

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path('stats'))
        if 'list' in result:
            trigger_manager = TriggerManager(self._client)
            triggers = []
            for stat in result['list']:
                if 'triggers' in stat and 'name' in stat:
                    if stat['name'] == tag:
                        for trigger_id in stat['triggers']:
                            triggers.append(trigger_manager.fetch_by_id(trigger_id))
                        return triggers
            return triggers
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def fetch_assigned_triggers_by_tags(self, tags):
        """
        Returns triggers assigned to at least one tag of tags

        :param tags: Iterable of tags
        :return: list of Trigger

        :raises: ResponseStructureError
        """

        tags = set(tags)
        result = self._client.get(self._full_path('stats'))
        if 'list' in result:
            trigger_manager = TriggerManager(self._client)
            triggers_id = set()
            for stat in result['list']:
                if 'triggers' in stat and 'name' in stat:
                    if stat['name'] in tags:
                        for trigger_id in stat['triggers']:
                            triggers_id.add(trigger_id)

            triggers = []
            for trigger_id in triggers_id:
                triggers.append(trigger_manager.fetch_by_id(trigger_id))

            return triggers
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def fetch_assigned_subscriptions(self, tag):
        """
        Returns subscriptions assigned to tag

        :param tag: str tag name
        :return: list of str subscription_id

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path('stats'))
        if 'list' in result:
            triggers = []
            for stat in result['list']:
                if 'subscriptions' in stat and 'name' in stat:
                    if stat['name'] == tag:
                        return [
                            Subscription(self._client, **subscription) for subscription in stat['subscriptions']
                            ]
            return triggers
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def _full_path(self, path=''):
        if path:
            return 'tag/' + path
        return 'tag'
