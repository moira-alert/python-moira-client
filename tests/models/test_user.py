try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.models.user import UserManager

from .test_model import ModelTest


class UserTest(ModelTest):

    def test_get_settings(self):
        client = Client(self.api_url)
        user_manager = UserManager(client)

        with patch.object(client, 'get', return_value={'login': 'aaa', 'contacts': [], 'subscriptions': []}
                          ) as get_mock:
            res_settings = user_manager.get_user_settings()

        self.assertEqual(res_settings.login, 'aaa')

        self.assertTrue(get_mock.called)

    def test_response_example_from_docs(self):
        client = Client(self.api_url)
        user_manager = UserManager(client)

        response = {
          "login": "john",
          "contacts": [
            {
              "id": "1dd38765-c5be-418d-81fa-7a5f879c2315",
              "user": "",
              "type": "mail",
              "value": "devops@example.com"
            }
          ],
          "subscriptions": [
            {
              "contacts": [
                "acd2db98-1659-4a2f-b227-52d71f6e3ba1"
              ],
              "tags": [
                "server",
                "cpu"
              ],
              "sched": {
                "days": [
                  {
                    "enabled": True,
                    "name": "Mon"
                  }
                ],
                "tzOffset": -60,
                "startOffset": 0,
                "endOffset": 1439
              },
              "plotting": {
                "enabled": True,
                "theme": "dark"
              },
              "id": "292516ed-4924-4154-a62c-ebe312431fce",
              "enabled": True,
              "any_tags": False,
              "ignore_warnings": False,
              "ignore_recoverings": False,
              "throttling": False,
              "user": ""
            }
          ]
        }

        with patch.object(client, 'get', return_value=response) as get_mock:
            res_settings = user_manager.get_user_settings()

        self.assertEqual(res_settings.login, 'john')
        self.assertEqual(res_settings.contacts[0].id, '1dd38765-c5be-418d-81fa-7a5f879c2315')

        self.assertTrue(get_mock.called)