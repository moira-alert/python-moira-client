try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from moira_client.client import Client
from moira_client.client import ResponseStructureError
from moira_client.models.health import HealthManager
from .test_model import ModelTest


class HealthTest(ModelTest):

    def test_get_notifier_state(self):
        client = Client(self.api_url)
        health_manager = HealthManager(client)

        with patch.object(client, 'get', return_value={'state': 'OK'}) as get_mock:
            health_manager.get_notifier_state()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('health/notifier')

    def test_get_notifier_state_bad_response(self):
        client = Client(self.api_url)
        health_manager = HealthManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                health_manager.get_notifier_state()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('health/notifier')

    def test_disable_notifications(self):
        client = Client(self.api_url)
        health_manager = HealthManager(client)

        with patch.object(client, 'put', return_value={'state': 'ERROR'}) as put_mock:
            res = health_manager.disable_notifications()

        data = {'state': 'ERROR'}
        
        self.assertTrue(put_mock.called)
        self.assertTrue(res)
        put_mock.assert_called_with('health/notifier', json=data)

    def test_disable_notifications_bad_response(self):
        client = Client(self.api_url)
        health_manager = HealthManager(client)

        with patch.object(client, 'put') as put_mock:
            with self.assertRaises(ResponseStructureError):
                health_manager.disable_notifications()

        data = {'state': 'ERROR'}
        
        self.assertTrue(put_mock.called)
        put_mock.assert_called_with('health/notifier', json=data)

    def test_enable_notifications(self):
        client = Client(self.api_url)
        health_manager = HealthManager(client)

        with patch.object(client, 'put', return_value={'state': 'OK'}) as put_mock:
            res = health_manager.enable_notifications()

        data = {'state': 'OK'}
        
        self.assertTrue(put_mock.called)
        self.assertTrue(res)
        put_mock.assert_called_with('health/notifier', json=data)

    def test_enable_notifications_bad_response(self):
        client = Client(self.api_url)
        health_manager = HealthManager(client)

        with patch.object(client, 'put') as put_mock:
            with self.assertRaises(ResponseStructureError):
                health_manager.enable_notifications()

        data = {'state': 'OK'}
        
        self.assertTrue(put_mock.called)
        put_mock.assert_called_with('health/notifier', json=data)
