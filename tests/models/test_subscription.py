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

    def test_create(self):
        client = Client(self.api_url)
        manager = SubscriptionManager(client)

        tags = ['server', 'cpu']
        contacts = ['acd2db98-1659-4a2f-b227-52d71f6e3ba1']
        s = manager.create(tags, contacts)

        with patch.object(client, 'put', return_value={"id": "e5cd5d73-d893-42b5-98b5-f9bd6c7bc501"}) as put_mock:
            s.save()

        self.assertTrue(put_mock.called)
        args_ = put_mock.call_args[1]
        body_json = args_['json']
        # check required fields
        self.assertEqual(tags, body_json['tags'])
        self.assertEqual(contacts, body_json['contacts'])
        # check default values
        self.assertEqual(True, body_json['enabled'])
        self.assertEqual(True, body_json['throttling'])
        self.assertTrue('sched' in body_json)
        self.assertEqual(False, body_json['ignore_warnings'])
        self.assertEqual(False, body_json['ignore_recoverings'])
        self.assertTrue('plotting' in body_json)
        self.assertEqual(False, body_json['any_tags'])

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
