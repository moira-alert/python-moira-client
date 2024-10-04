from moira_client.client import Client
from moira_client.models.team import TeamManager, TeamModel
from ._mock import patch, Mock
from ..test_model import ModelTest


class TestTeamManager(ModelTest):
    def __init__(self, *args, **kwargs) -> None:
        self._client = Client(self.api_url)
        self._manager = TeamManager(self._client)
        super().__init__(*args, **kwargs)

    @property
    def _request_data(self) -> dict:
        return {
            "name": "Infrastructure Team",
            "description": "Team that holds all members of infrastructure division",
        }

    @property
    def _single_response_data(self) -> dict:
        return {
            "id": "d5d98eb3-ee18-4f75-9364-244f67e23b54",
        }

    @property
    def _response_data(self) -> dict:
        return {
            **self._single_response_data,
            **self._request_data,
        }

    @property
    def _team(self) -> TeamModel:
        return TeamModel(
            id="d5d98eb3-ee18-4f75-9364-244f67e23b54",
            name="Infrastructure Team",
            description="Team that holds all members of infrastructure division",
        )

    @staticmethod
    def _assert_is_resource_request(request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams"

    def _assert_is_object_request(self, request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams/{team_id}".format(team_id=self._team.id)

    def _assert_is_request_data_sent(self, request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 1
        assert kwargs["json"] == self._request_data

    @staticmethod
    def _assert_is_no_data_sent(request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 0

    def test_get_all(self) -> None:
        return_value = {
            "teams": [
                self._response_data,
            ],
        }

        with patch.object(self._client, "get", return_value=return_value) as request:
            response = self._manager.get_all()

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_no_data_sent(request)

        assert len(response.teams) == 1
        assert response.teams[0].id == self._response_data["id"]
        assert response.teams[0].name == self._response_data["name"]
        assert response.teams[0].description == self._response_data["description"]

    def test_create(self):
        with patch.object(self._client, "post", return_value=self._single_response_data) as request:
            response = self._manager.create(self._team)

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_request_data_sent(request)

        assert response.id == self._single_response_data["id"]

    def test_delete(self):
        with patch.object(self._client, "delete", return_value=self._single_response_data) as request:
            response = self._manager.delete(self._team.id)

        assert len(request.mock_calls) == 1
        self._assert_is_object_request(request)
        self._assert_is_no_data_sent(request)

        assert response.id == self._single_response_data["id"]

    def test_get(self):
        with patch.object(self._client, "get", return_value=self._response_data) as request:
            response = self._manager.get(self._team.id)

        assert len(request.mock_calls) == 1
        self._assert_is_object_request(request)
        self._assert_is_no_data_sent(request)

        assert response.id == self._response_data["id"]
        assert response.name == self._response_data["name"]
        assert response.description == self._response_data["description"]

    def test_update(self):
        with patch.object(self._client, "put", return_value=self._single_response_data) as request:
            response = self._manager.update(self._team.id, self._team)

        assert len(request.mock_calls) == 1
        self._assert_is_object_request(request)
        self._assert_is_request_data_sent(request)

        assert response.id == self._single_response_data["id"]
