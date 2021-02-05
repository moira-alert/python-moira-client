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
        result = self.fetch(start=0, end=-1)
        return result

    def fetch(self, start, end):
        """
        Gets a paginated list of notifications
        :return: list of dict

        :param start
        :param end

        :raises: ResponseStructureError
        """
        params = {
            'start': start,
            'end': end
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

    def delete(self, notification_id):
        """
        Remove notification by id

        :param notification_id: str notification id

        :return: True on success, False otherwise
        """

        params = {
            'id': notification_id,
        }
        try:
            result = self._client.delete(self._full_path(), params=params)
            if 'result' in result and result['result'] == 0:
                return True
        except InvalidJSONError as e:
            return False

    def _full_path(self, path=''):
        if path:
            return 'notification/{}'.format(path)
        return 'notification'
