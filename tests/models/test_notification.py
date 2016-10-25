try:
    from unittest.mock import patch
except:
    from mock import patch

from moira_client.client import Client
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
        get_mock.assert_called_with('notification/', params=params)

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        contact_manager = NotificationManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                contact_manager.fetch_all()

        params = {'end': -1, 'start': 0}

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('notification/', params=params)
