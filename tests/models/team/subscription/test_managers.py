from moira_client.client import Client
from moira_client.models.subscription import SubscriptionModel
from moira_client.models.team.subscription import TeamSubscriptionManager
from .._mock import patch, Mock
from ...test_model import ModelTest


class TestTeamSubscriptionManager(ModelTest):
    def __init__(self, *args, **kwargs) -> None:
        self._client = Client(self.api_url)
        self._manager = TeamSubscriptionManager(self._client)
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

    @property
    def _subscription(self) -> SubscriptionModel:
        return SubscriptionModel(**self._request_data)

    def _assert_is_resource_request(self, request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams/{team_id}/subscriptions".format(
            team_id=self._subscription.team_id,
        )

    def _assert_is_request_data_sent(self, request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 1
        assert kwargs["json"] == self._request_data

    def test_create(self) -> None:
        with patch.object(self._client, "post", return_value=self._response_data) as request:
            response = self._manager.create(self._subscription.team_id, self._subscription)

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_request_data_sent(request)

        assert response.team_id == self._response_data["team_id"]
        assert response.contacts == self._response_data["contacts"]
        assert response.tags == self._response_data["tags"]
        assert response.enabled == self._response_data["enabled"]
        assert response.any_tags == self._response_data["any_tags"]
        assert response.throttling == self._response_data["throttling"]
        assert response.sched == self._response_data["sched"]
        assert response.ignore_warnings == self._response_data["ignore_warnings"]
        assert response.ignore_recoverings == self._response_data["ignore_recoverings"]
        assert response.plotting == self._response_data["plotting"]
