from moira_client.client import Client
from moira_client.models.contact import Contact
from moira_client.models.team.contact import TeamContactManager
from .._mock import patch, Mock
from ...test_model import ModelTest


class TestTeamContactManager(ModelTest):
    def __init__(self, *args, **kwargs) -> None:
        self._client = Client(self.api_url)
        self._manager = TeamContactManager(self._client)
        super().__init__(*args, **kwargs)

    @property
    def _request_data(self) -> dict:
        return {
            "name": "Mail Alerts",
            "team_id": "string",
            "type": "mail",
            "user": "",
            "value": "devops@example.com",
        }

    @property
    def _response_data(self) -> dict:
        return {
            "id": "1dd38765-c5be-418d-81fa-7a5f879c2315",
            "name": "Mail Alerts",
            "team_id": "string",
            "type": "mail",
            "user": "",
            "value": "devops@example.com",
        }

    @property
    def _contact(self) -> Contact:
        return Contact(**self._request_data)

    def _assert_is_resource_request(self, request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams/{team_id}/contacts".format(team_id=self._contact.team_id)

    def _assert_is_request_data_sent(self, request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 1
        assert kwargs["json"] == self._request_data

    def test_create(self) -> None:
        with patch.object(self._client, "post", return_value=self._response_data) as request:
            response = self._manager.create(self._contact.team_id, self._contact)

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_request_data_sent(request)

        assert response.id == self._response_data["id"]
        assert response.name == self._response_data["name"]
        assert response.team_id == self._response_data["team_id"]
        assert response.type == self._response_data["type"]
        assert response.user == self._response_data["user"]
        assert response.value == self._response_data["value"]
