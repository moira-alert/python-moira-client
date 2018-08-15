from ..client import InvalidJSONError
from ..client import ResponseStructureError


class NotificationManager:
    def __init__(self, client):
        self._client = client

    def fetch_all(self):
        """
        Returns all notifications
        :return: list of dict

        :raises: ResponseStructureError
        """
        params = {
            'start': 0,
            'end': -1
        }
        result = self._client.get(self._full_path(), params=params)
        if 'list' not in result:
            raise ResponseStructureError("list doesn't exist in response", result)

        return result['list']

    def delete_all(self):
        """
        Remove all notifications

        :return: True on success, False otherwise
        """
        try:
            result = self._client.delete(self._full_path("all"))
            return False
        except InvalidJSONError as e:
            if e.content == b'':  # successfully if response is blank
                return True
            return False

    def _full_path(self, path=''):
        if path:
            return 'notification/' + path
        return 'notification'
