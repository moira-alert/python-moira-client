from typing import Optional

from ._models import TeamModel, UserTeams, SaveTeamResponse
from .contact import TeamContactManager
from .settings import TeamSettingsManager
from .subscription import TeamSubscriptionManager
from .user import TeamUserManager
from ...client import Client


class TeamManager:
    def __init__(self, client: Client) -> None:
        self._client = client
        self._user = None  # type: Optional[TeamUserManager]
        self._settings = None  # type: Optional[TeamSettingsManager]
        self._subscription = None  # type: Optional[TeamSubscriptionManager]
        self._contact = None  # type: Optional[TeamContactManager]

    def get_all(self) -> UserTeams:
        """Get all teams"""
        response = self._client.get(self._full_path())

        return UserTeams(teams=[TeamModel(**team) for team in response["teams"]])

    def create(self, team: TeamModel) -> SaveTeamResponse:
        """Create a new team"""
        payload = {
            "name": team.name,
            "description": team.description,
        }

        response = self._client.post(self._full_path(), json=payload)

        return SaveTeamResponse(**response)

    def delete(self, team_id: str) -> SaveTeamResponse:
        """Delete a team"""
        response = self._client.delete(self._full_path(team_id))

        return SaveTeamResponse(**response)

    def get(self, team_id: str) -> TeamModel:
        """Get a team by ID"""
        response = self._client.get(self._full_path(team_id))

        return TeamModel(**response)

    def update(self, team_id: str, team: TeamModel) -> SaveTeamResponse:
        """Update existing team"""
        payload = {
            "name": team.name,
            "description": team.description,
        }

        response = self._client.put(self._full_path(team_id), json=payload)

        return SaveTeamResponse(**response)

    @property
    def user(self) -> TeamUserManager:
        """Get team user manager"""
        if self._user is None:
            self._user = TeamUserManager(self._client)

        return self._user

    @property
    def settings(self) -> TeamSettingsManager:
        """Get team settings manager"""
        if self._settings is None:
            self._settings = TeamSettingsManager(self._client)

        return self._settings

    @property
    def subscription(self) -> TeamSubscriptionManager:
        """Get team subscription manager"""
        if self._subscription is None:
            self._subscription = TeamSubscriptionManager(self._client)

        return self._subscription

    @property
    def contact(self) -> TeamContactManager:
        """Get team contact manager"""
        if self._contact is None:
            self._contact = TeamContactManager(self._client)

        return self._contact

    @staticmethod
    def _full_path(team_id: Optional[str] = None) -> str:
        if team_id is None:
            return "teams"

        return "teams/{team_id}".format(team_id=team_id)
