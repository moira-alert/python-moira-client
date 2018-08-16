try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.client import InvalidJSONError
from moira_client.client import ResponseStructureError
from moira_client.models.notification import NotificationManager
from .test_model import ModelTest


class NotificationTest(ModelTest):

    def test_fetch_all(self):
        client = Client(self.api_url)
        contact_manager = NotificationManager(client)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            contact_manager.fetch_all()

        params = {'end': -1, 'start': 0}

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('notification', params=params)

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        contact_manager = NotificationManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                contact_manager.fetch_all()

        params = {'end': -1, 'start': 0}

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('notification', params=params)

    def test_delete_all(self):
        client = Client(self.api_url)
        notification_manager = NotificationManager(client)

        with patch.object(client, 'delete', new=Mock(side_effect=InvalidJSONError(b''))) as delete_mock:
            res = notification_manager.delete_all()

        self.assertTrue(delete_mock.called)
        self.assertTrue(res)
        delete_mock.assert_called_with('notification/all')

    def test_delete_all_bad_response(self):
        client = Client(self.api_url)
        notification_manager = NotificationManager(client)

        with patch.object(client, 'delete') as delete_mock:
            res = notification_manager.delete_all()

        self.assertTrue(delete_mock.called)
        self.assertFalse(res)
        delete_mock.assert_called_with('notification/all')
