from collections import namedtuple

from ..client import InvalidJSONError
from ..client import ResponseStructureError
from .trigger import Trigger


Pattern = namedtuple('Pattern', ['metrics', 'pattern', 'triggers'])


class PatternManager:
    """
    A Graphite pattern is a single dot-separated metric name, possibly containing one or more wildcards.
    """
    def __init__(self, client):
        self._client = client

    def fetch_all(self):
        """
        Returns all existing patterns in all triggers

        :return: list of Pattern

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())
        if 'list' in result:
            patterns = []
            for pattern in result['list']:
                if 'triggers' in pattern:
                    pattern['triggers'] = [Trigger(self._client, **trigger) for trigger in pattern['triggers']]
                patterns.append(Pattern(**pattern))
            return patterns
        else:
            raise ResponseStructureError("list doesn't exist in response", result)

    def delete(self, pattern):
        """
        Delete pattern
        Returns True even if pattern doesn't exist

        :param pattern: str pattern
        :return: True if deleted, False otherwise

        :raises: ResponseStructureError
        """
        try:
            self._client.delete(self._full_path(pattern))
            return False
        except InvalidJSONError:
            return True

    def _full_path(self, path=''):
        return 'pattern/' + path
