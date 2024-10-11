from moira_client.client import Client
from moira_client.models.subscription import Subscription
from .._mock import patch, Mock
from ...test_model import ModelTest


class TestSubscription(ModelTest):
    def __init__(self, *args, **kwargs) -> None:
        self._client = Client(self.api_url)
        super().__init__(*args, **kwargs)

    @property
    def _request_data(self) -> dict:
        return {
            "team_id": "324516ed-4924-4154-a62c-eb124234fce",
            "contacts": [
                "acd2db98-1659-4a2f-b227-52d71f6e3ba1",
            ],
            "tags": [
                "server",
                "cpu",
            ],
            "enabled": True,
            "any_tags": False,
            "throttling": False,
            "sched": {
                "days": [
                    {
                        "enabled": True,
                        "name": "Mon",
                    },
                ],
                "endOffset": 1439,
                "startOffset": 0,
                "tzOffset": -60,
            },
            "ignore_warnings": False,
            "ignore_recoverings": False,
            "plotting": {
                "enabled": True,
                "theme": "dark",
            },
        }

    @property
    def _response_data(self) -> dict:
        return {
            "id": "292516ed-4924-4154-a62c-ebe312431fce",
            **self._request_data,
        }

    @staticmethod
    def _assert_is_resource_request(request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "subscription"

    def _assert_is_request_data_sent(self, request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 1
        assert kwargs["json"] == self._request_data

    def test_save(self) -> None:
        subscription = Subscription(self._client, **self._request_data)

        with patch.object(self._client, "put", return_value=self._response_data) as request:
            subscription.save()

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_request_data_sent(request)

        assert subscription.id == self._response_data["id"]
        assert subscription.team_id == self._response_data["team_id"]
        assert subscription.contacts == self._response_data["contacts"]
        assert subscription.tags == self._response_data["tags"]
        assert subscription.enabled == self._response_data["enabled"]
        assert subscription.any_tags == self._response_data["any_tags"]
        assert subscription.throttling == self._response_data["throttling"]
        assert subscription.sched == self._response_data["sched"]
        assert subscription.ignore_warnings == self._response_data["ignore_warnings"]
        assert subscription.ignore_recoverings == self._response_data["ignore_recoverings"]
        assert subscription.plotting == self._response_data["plotting"]
