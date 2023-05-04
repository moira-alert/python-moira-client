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
    QUERY_PARAM_VALIDATE_FLAG = 'validate'

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

    def test_setMaintenance(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'
        end_timestamp = 1612260000

        with patch.object(client, 'put') as put_mock:
            res = trigger_manager.set_maintenance(trigger_id, end_timestamp)

        self.assertTrue(put_mock.called)
        self.assertTrue(res)
        expected_request_data = {
            'trigger': end_timestamp,
        }
        put_mock.assert_called_with('trigger/' + trigger_id + '/setMaintenance', json=expected_request_data)

    def test_setMaintenance_with_metrics(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'
        end_timestamp = 1612260000
        metrics = {
            'metric': end_timestamp,
            'metric2': 1612260555,
        }

        with patch.object(client, 'put') as put_mock:
            res = trigger_manager.set_maintenance(trigger_id, end_timestamp, metrics)

        self.assertTrue(put_mock.called)
        self.assertTrue(res)
        expected_request_data = {
            'trigger': end_timestamp,
            'metrics': metrics,
        }
        put_mock.assert_called_with('trigger/' + trigger_id + '/setMaintenance', json=expected_request_data)

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

    def test_save_new_trigger(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger = trigger_manager.create('Name', ['tag'], ['target'])

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            trigger_id = '1'

            with patch.object(client, 'put', return_value={'id': trigger_id}) as put_mock:
                result = trigger.save()

                self.assertTrue(get_mock.called)
                self.assertTrue(put_mock.called)
                self.assertEqual(put_mock.call_args[0][0], f'trigger?{self.QUERY_PARAM_VALIDATE_FLAG}')
                self.assertEqual(result['id'], trigger_id)

    def test_save_existing_trigger(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'

        state = {
            'state': 'OK',
            'trigger_id': trigger_id
        }
        trigger = {
            'name': 'Name',
            'tags': ['tag'],
            'targets': ['target'],
        }
        trigger_from_response = {
            'id': trigger_id,
            **trigger
        }

        with patch.object(client, 'get', side_effect=[{'list': [trigger_from_response]}, state, trigger_from_response]) as get_mock:
            trigger_dto = trigger_manager.create(**trigger)
            with patch.object(client, 'put', return_value={'id': trigger_id}) as put_mock:
                result = trigger_dto.save()

                self.assertTrue(get_mock.called)
                self.assertTrue(put_mock.called)
                self.assertEqual(put_mock.call_args[0][0], f'trigger/{trigger_id}?{self.QUERY_PARAM_VALIDATE_FLAG}')
                self.assertEqual(result['id'], trigger_id)

    def test_save_trigger_with_id(self):
        client = Client(self.api_url)
        trigger_manager = TriggerManager(client)

        trigger_id = '1'
        state = {
            'state': 'OK',
            'trigger_id': trigger_id
        }
        trigger = {
            'id': trigger_id,
            'name': 'Name',
            'tags': ['tag'],
            'targets': ['target'],
        }

        with patch.object(client, 'get', side_effect=[state, trigger]) as get_mock:
            trigger_dto = trigger_manager.create(**trigger)
            with patch.object(client, 'put', return_value={'id': trigger_id}) as put_mock:
                result = trigger_dto.save()

                self.assertTrue(get_mock.called)
                self.assertTrue(put_mock.called)
                self.assertEqual(put_mock.call_args[0][0], f'trigger/{trigger_id}?{self.QUERY_PARAM_VALIDATE_FLAG}')
                self.assertEqual(result['id'], trigger_id)
