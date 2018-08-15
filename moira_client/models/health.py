STATE_OK: "OK"
STATE_ERROR: "ERROR"


class HealthManager:
    def __init__(self, client):
        self._client = client

    def disable_notifier(self):
        """
        Manages Moira Notifier to stop sending notifications
        :return: bool
        """
        params = {
            'state': STATE_ERROR
        }
        result = self._client.get(self._full_path("notifier"))
        return result

    def enable_notifier(self):
        """
        Manages Moira Notifier to start sending notifications
        :return: bool
        """
        params = {
            'state': STATE_OK
        }
        result = self._client.get(self._full_path("notifier"))
        return result

    def _full_path(self, path=''):
        if path:
            return 'health/' + path
        return 'health'
