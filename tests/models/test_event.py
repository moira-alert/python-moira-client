try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from moira_client.client import Client
from moira_client.client import ResponseStructureError
from moira_client.models.event import EventManager
from moira_client.models.event import MAX_FETCH_LIMIT
from moira_client.models.trigger import Trigger
from .test_model import ModelTest


class EventTest(ModelTest):

    def test_fetch_by_trigger(self):
        client = Client(self.api_url)
        contact_manager = EventManager(client)

        trigger_id = '1'
        trigger = Trigger(client, 'Name', ['tag'], ['target'], 0, 1, id=trigger_id)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            contact_manager.fetch_by_trigger(trigger)

        self.assertTrue(get_mock.called)

        expected_request_data = {
            'p': 0,
            'size': MAX_FETCH_LIMIT
        }

        get_mock.assert_called_with('event/' + trigger_id, params=expected_request_data)

    def test_fetch_by_trigger_bad_response(self):
        client = Client(self.api_url)
        contact_manager = EventManager(client)

        trigger_id = '1'
        trigger = Trigger(client, 'Name', ['tag'], ['target'], 0, 1, id=trigger_id)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                contact_manager.fetch_by_trigger(trigger)

        self.assertTrue(get_mock.called)

        expected_request_data = {
            'p': 0,
            'size': MAX_FETCH_LIMIT
        }

        get_mock.assert_called_with('event/' + trigger_id, params=expected_request_data)
