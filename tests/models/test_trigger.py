try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.client import InvalidJSONError
from moira_client.client import ResponseStructureError
from moira_client.models.trigger import TriggerManager
from .test_model import ModelTest


class TriggerTest(ModelTest):

    def test_fetch_all(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            trigger_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('trigger')

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                trigger_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('trigger')

    def test_delete_fail(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'

        with patch.object(client, 'delete') as delete_mock:
            res = trigger_manager.delete(trigger_id)

        self.assertTrue(delete_mock.called)
        self.assertFalse(res)
        delete_mock.assert_called_with('trigger/' + trigger_id)

    def test_delete(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'

        with patch.object(client, 'delete', new=Mock(side_effect=InvalidJSONError(b''))) as delete_mock:
            res = trigger_manager.delete(trigger_id)

        self.assertTrue(delete_mock.called)
        self.assertTrue(res)
        delete_mock.assert_called_with('trigger/' + trigger_id)

    def test_fetch_by_id(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'

        state = {
            'state': 'OK',
            'trigger_id': trigger_id
            }

        trigger = {
            'id': trigger_id,
            'name': 'trigger_name',
            'tags': ['tag'],
            'targets': ['pattern'],
            'warn_value': 0,
            'error_value': 1
            }

        with patch.object(client, 'get', side_effect=[state, trigger]) as get_mock:
            trigger = trigger_manager.fetch_by_id(trigger_id)

            self.assertTrue(get_mock.called)
            self.assertEqual(trigger_id, trigger.id)
