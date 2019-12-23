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

        with patch.object(client, "get", return_value={"list": []}) as get_mock:
            subscription_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with("subscription")

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        with patch.object(client, "get", return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                subscription_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with("subscription")

    def test_create_and_save_with_empty_sched_days(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription = subscription_manager.create(
            tags=["tag1", "tag2"],
            contacts=["contact_id"],
            sched={"days": None, "tzOffset": 0, "startOffset": 0, "endOffset": 0},
            ignore_warnings=False,
            ignore_recoverings=False,
            plotting={"enabled": False, "theme": ""},
        )

        with patch.object(client, "put", return_value={"id": "sub_id"}) as put_mock:
            subscription.save()

        self.assertTrue(put_mock.called)
        put_mock.assert_called_with(
            "subscription",
            json={
                "contacts": ["contact_id"],
                "tags": ["tag1", "tag2"],
                "enabled": True,
                "throttling": True,
                "sched": {
                    "days": [
                        {"enabled": True, "name": "Mon"},
                        {"enabled": True, "name": "Tue"},
                        {"enabled": True, "name": "Wed"},
                        {"enabled": True, "name": "Thu"},
                        {"enabled": True, "name": "Fri"},
                        {"enabled": True, "name": "Sat"},
                        {"enabled": True, "name": "Sun"},
                    ],
                    "tzOffset": 0,
                    "startOffset": 0,
                    "endOffset": 0,
                },
                "ignore_warnings": False,
                "ignore_recoverings": False,
                "plotting": {"enabled": False, "theme": ""},
            },
        )

    def test_delete(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = "1"

        with patch.object(
            client, "delete", new=Mock(side_effect=InvalidJSONError(b""))
        ) as delete_mock:
            res = subscription_manager.delete(subscription_id)

        self.assertTrue(delete_mock.called)
        self.assertTrue(res)
        delete_mock.assert_called_with("subscription/" + subscription_id)

    def test_delete_fail(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = "1"

        with patch.object(client, "delete") as delete_mock:
            res = subscription_manager.delete(subscription_id)

        self.assertTrue(delete_mock.called)
        self.assertFalse(res)
        delete_mock.assert_called_with("subscription/" + subscription_id)

    def test_test(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = "1"

        with patch.object(
            client, "put", new=Mock(side_effect=InvalidJSONError(b""))
        ) as put_mock:
            res = subscription_manager.test(subscription_id)

        self.assertTrue(put_mock.called)
        self.assertTrue(res)
        put_mock.assert_called_with("subscription/" + subscription_id + "/test")

    def test_test_fail(self):
        client = Client(self.api_url)
        subscription_manager = SubscriptionManager(client)

        subscription_id = "1"

        with patch.object(client, "put") as put_mock:
            res = subscription_manager.test(subscription_id)

        self.assertTrue(put_mock.called)
        self.assertFalse(res)
        put_mock.assert_called_with("subscription/" + subscription_id + "/test")
