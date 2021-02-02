try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.client import ResponseStructureError
from .test_model import ModelTest
from moira_client.models.config import ConfigManager, WebContact


class ConfigTest(ModelTest):

    def test_fetch(self):
        client = Client(self.api_url)
        config_manager = ConfigManager(client)

        with patch.object(client, 'get', return_value={'remoteAllowed': True, 'contacts': []}) as get_mock:
            res = config_manager.fetch()

        self.assertTrue(get_mock.called)

    def test_fetch_with_contacts(self):
        client = Client(self.api_url)
        config_manager = ConfigManager(client)

        with patch.object(client, 'get', return_value={'remoteAllowed': True,
                                                       'contacts': [{'label': 'Telegram', 'type': 'telegram'}]}
                          ) as get_mock:
            res = config_manager.fetch()
        self.assertTrue(res.remoteAllowed)

        self.assertEqual(res.contacts[0].type, 'telegram')
        self.assertEqual(res.contacts[0].label, 'Telegram')
        self.assertTrue(get_mock.called)

    def test_fetch_fail_without_required_fields(self):
        client = Client(self.api_url)
        config_manager = ConfigManager(client)

        with patch.object(client, 'get', return_value={'remoteAllowed': True}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                config_manager.fetch()
        self.assertTrue(get_mock.called)

        with patch.object(client, 'get', return_value={'contacts': True}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                config_manager.fetch()
        self.assertTrue(get_mock.called)
