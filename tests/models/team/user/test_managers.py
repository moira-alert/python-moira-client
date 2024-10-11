from moira_client.client import Client
from moira_client.models.team.user import TeamUserManager, TeamMembers
from .._mock import patch, Mock
from ...test_model import ModelTest


class TestTeamUserManager(ModelTest):
    def __init__(self, *args, **kwargs) -> None:
        self._client = Client(self.api_url)
        self._manager = TeamUserManager(self._client)
        super().__init__(*args, **kwargs)

    @property
    def _request_data(self) -> dict:
        return {
            "usernames": ["anonymous"],
        }

    @property
    def _response_data(self) -> dict:
        return self._request_data

    @property
    def _users(self) -> TeamMembers:
        return TeamMembers(**self._request_data)

    @property
    def _team_id(self) -> str:
        return "d5d98eb3-ee18-4f75-9364-244f67e23b54"

    def _assert_is_resource_request(self, request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams/{team_id}/users".format(team_id=self._team_id)

    def _assert_is_object_request(self, request: Mock) -> None:
        args = request.call_args[0]
        assert len(args) == 1
        assert args[0] == "teams/{team_id}/users/{team_user_id}".format(
            team_id=self._team_id,
            team_user_id=self._users.usernames[0],
        )

    def _assert_is_request_data_sent(self, request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 1
        assert kwargs["json"] == self._request_data

    @staticmethod
    def _assert_is_no_data_sent(request: Mock) -> None:
        kwargs = request.call_args[1]
        assert len(kwargs) == 0

    def _assert_response(self, response) -> None:
        assert len(response.usernames) == 1
        assert response.usernames[0] == self._response_data["usernames"][0]

    def test_get(self) -> None:
        with patch.object(self._client, "get", return_value=self._response_data) as request:
            self._assert_response(self._manager.get(self._team_id))

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_no_data_sent(request)

    def test_add(self) -> None:
        with patch.object(self._client, "post", return_value=self._response_data) as request:
            self._assert_response(self._manager.add(self._team_id, self._users))

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_request_data_sent(request)

    def test_set(self) -> None:
        with patch.object(self._client, "put", return_value=self._response_data) as request:
            self._assert_response(self._manager.set(self._team_id, self._users))

        assert len(request.mock_calls) == 1
        self._assert_is_resource_request(request)
        self._assert_is_request_data_sent(request)

    def test_delete(self) -> None:
        with patch.object(self._client, "delete", return_value=self._response_data) as request:
            self._assert_response(self._manager.delete(self._team_id, self._users.usernames[0]))

        assert len(request.mock_calls) == 1
        self._assert_is_object_request(request)
        self._assert_is_no_data_sent(request)
