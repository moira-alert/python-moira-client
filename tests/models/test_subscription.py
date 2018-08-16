try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.client import InvalidJSONError
from moira_client.client import ResponseStructureError
from moira_client.models.subscription import SubscriptionManager
from .test_model import ModelTest


class SubscriptionTest(ModelTest):

    def test_fetch_all(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            subscription_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('subscription')

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                subscription_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('subscription') 

    def test_delete(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = '1'

        with patch.object(client, 'delete', new=Mock(side_effect=InvalidJSONError(b''))) as delete_mock:
            res = subscription_manager.delete(subscription_id)

        self.assertTrue(delete_mock.called)
        self.assertTrue(res)
        delete_mock.assert_called_with('subscription/' + subscription_id)

    def test_delete_fail(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = '1'

        with patch.object(client, 'delete') as delete_mock:
            res = subscription_manager.delete(subscription_id)

        self.assertTrue(delete_mock.called)
        self.assertFalse(res)
        delete_mock.assert_called_with('subscription/' + subscription_id)

    def test_test(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = '1'

        with patch.object(client, 'put', new=Mock(side_effect=InvalidJSONError(b''))) as put_mock:
            res = subscription_manager.test(subscription_id)

        self.assertTrue(put_mock.called)
        self.assertTrue(res)
        put_mock.assert_called_with('subscription/' + subscription_id + '/test')

    def test_test_fail(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = '1'

        with patch.object(client, 'put') as put_mock:
            res = subscription_manager.test(subscription_id)

        self.assertTrue(put_mock.called)
        self.assertFalse(res)
        put_mock.assert_called_with('subscription/' + subscription_id + '/test')
