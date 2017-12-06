try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.client import InvalidJSONError
from moira_client.client import ResponseStructureError
from moira_client.models.pattern import PatternManager
from .test_model import ModelTest


class PatternTest(ModelTest):

    def test_fetch_all(self):
        client = Client(self.api_url)
        pattern_manager = PatternManager(client)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            pattern_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('pattern')

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        pattern_manager = PatternManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                pattern_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('pattern')

    def test_delete(self):
        client = Client(self.api_url)
        pattern_manager = PatternManager(client)

        pattern_id = '1'

        with patch.object(client, 'delete', new=Mock(side_effect=InvalidJSONError(b''))) as delete_mock:
            res = pattern_manager.delete(pattern_id)

        self.assertTrue(delete_mock.called)
        self.assertTrue(res)
        delete_mock.assert_called_with('pattern/' + pattern_id)

    def test_delete_fail(self):
        client = Client(self.api_url)
        pattern_manager = PatternManager(client)

        pattern_id = '1'

        with patch.object(client, 'delete') as delete_mock:
            res = pattern_manager.delete(pattern_id)

        self.assertTrue(delete_mock.called)
        self.assertFalse(res)
        delete_mock.assert_called_with('pattern/' + pattern_id)
