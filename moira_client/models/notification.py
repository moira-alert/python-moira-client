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

    def _full_path(self, path=''):
        return 'notification/' + path
