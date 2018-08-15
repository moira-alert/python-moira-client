from ..client import ResponseStructureError


class HealthManager:
    def __init__(self, client):
        self._client = client

    def get_notifier_state(self):
        """
        Returns current Moira Notifier state
        :return: str

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path("notifier"))
        if 'state' not in result:
            raise ResponseStructureError("state doesn't exist in response", result)

        return result['state']

    def disable_notifier(self):
        """
        Manages Moira Notifier to stop sending notifications
        Returns current Moira Notifier state
        :return: str

        :raises: ResponseStructureError
        """
        data = {
            'state': "ERROR"
        }
        result = self._client.put(self._full_path("notifier"), json=data)
        if 'state' not in result:
            raise ResponseStructureError("state doesn't exist in response", result)

        return result['state']

    def enable_notifier(self):
        """
        Manages Moira Notifier to start sending notifications
        Returns current Moira Notifier state
        :return: str

        :raises: ResponseStructureError
        """
        data = {
            'state': "OK"
        }
        result = self._client.put(self._full_path("notifier"), json=data)
        if 'state' not in result:
            raise ResponseStructureError("state doesn't exist in response", result)

        return result['state']

    def _full_path(self, path=''):
        if path:
            return 'health/' + path
        return 'health'
