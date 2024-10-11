from moira_client.client import Client
from moira_client.models.team.settings import TeamSettingsManager
from .._mock import patch, Mock
from ...test_model import ModelTest


class TestTeamSettingsManager(ModelTest):
    def __init__(self, *args, **kwargs) -> None:
        self._client = Client(self.api_url)
        self._manager = TeamSettingsManager(self._client)
        super().__init__(*args, **kwargs)

    @property
    def _response_data_contact(self) -> dict:
        return {
            "id": "1dd38765-c5be-418d-81fa-7a5f879c2315",
            "name": "Mail Alerts",
            "team_id": "string",
            "type": "mail",
            "user": "",
            "value": "devops@example.com",
        }

    @property
    def _response_data_subscription(self) -> dict:
        return {
            "any_tags": False,
            "contacts": [
                "acd2db98-1659-4a2f-b227-52d71f6e3ba1",
            ],
            "enabled": True,
            "id": "292516ed-4924-4154-a62c-ebe312431fce",
            "ignore_recoverings": False,
            "ignore_warnings": False,
            "plotting": {
                "enabled": True,
                "theme": "dark",
            },
            "sched": {
                "days": [
                    {
                        "enabled": True,
                        "name": "Mon",
                    }
                ],
                "endOffset": 1439,
                "startOffset": 0,
                "tzOffset": -60,
            },
            "tags": [
                "server",
                "cpu",
            ],
            "team_id": "324516ed-4924-4154-a62c-eb124234fce",
            "throttling": False,
            "user": "",
        }

    @property
    def _team_id(self) -> str:
        return "d5d98eb3-ee18-4f75-9364-244f67e23b54"

    @property
    def _response_data(self) -> dict:
        return {
            "contacts": [
                self._response_data_contact,
            ],
            "subscriptions": [
                self._response_data_subscription,
            ],
            "team_id": self._team_id,
        }

    def _assert_is_resource_request(self, request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams/{team_id}/settings".format(team_id=self._team_id)

    @staticmethod
    def _assert_is_no_data_sent(request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 0

    def test_get_all(self) -> None:
        with patch.object(self._client, "get", return_value=self._response_data) as request:
            response = self._manager.get(self._team_id)

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_no_data_sent(request)

        assert response.team_id == self._team_id

        assert len(response.contacts) == 1

        assert response.contacts[0].id == self._response_data_contact["id"]
        assert response.contacts[0].name == self._response_data_contact["name"]
        assert response.contacts[0].team_id == self._response_data_contact["team_id"]
        assert response.contacts[0].type == self._response_data_contact["type"]
        assert response.contacts[0].user == self._response_data_contact["user"]
        assert response.contacts[0].value == self._response_data_contact["value"]

        assert len(response.subscriptions) == 1

        assert response.subscriptions[0].team_id == self._response_data_subscription["team_id"]
        assert response.subscriptions[0].contacts == self._response_data_subscription["contacts"]
        assert response.subscriptions[0].tags == self._response_data_subscription["tags"]
        assert response.subscriptions[0].enabled == self._response_data_subscription["enabled"]
        assert response.subscriptions[0].any_tags == self._response_data_subscription["any_tags"]
        assert response.subscriptions[0].throttling == self._response_data_subscription["throttling"]
        assert response.subscriptions[0].sched == self._response_data_subscription["sched"]
        assert response.subscriptions[0].ignore_warnings == self._response_data_subscription["ignore_warnings"]
        assert response.subscriptions[0].ignore_recoverings == self._response_data_subscription["ignore_recoverings"]
        assert response.subscriptions[0].plotting == self._response_data_subscription["plotting"]
