try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch
from moira_client.client import Client
from moira_client.models.system_tag import SystemTagManager
from .test_model import ModelTest


class SystemTagTest(ModelTest):

    def test_fetch_all(self):
        client = Client(self.api_url)
        system_tag_manager = SystemTagManager(client)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            system_tag_manager.fetch_all()
        
        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('tag')
