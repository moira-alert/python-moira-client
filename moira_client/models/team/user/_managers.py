from ._models import TeamMembers
from ....client import Client
from typing import Optional


class TeamUserManager:
    def __init__(self, client: Client) -> None:
        self._client = client

    def get(self, team_id: str) -> TeamMembers:
        """Get users of a team"""
        response = self._client.get(self._full_path(team_id))

        return TeamMembers(**response)

    def add(self, team_id: str, members: TeamMembers) -> TeamMembers:
        """Add users to a team"""
        payload = {"usernames": members.usernames}

        response = self._client.post(self._full_path(team_id), json=payload)

        return TeamMembers(**response)

    def set(self, team_id: str, members: TeamMembers) -> TeamMembers:
        """Set users of a team"""
        payload = {"usernames": members.usernames}

        response = self._client.put(self._full_path(team_id), json=payload)

        return TeamMembers(**response)

    def delete(self, team_id: str, team_user_id: str) -> TeamMembers:
        """Delete a user from a team"""
        response = self._client.delete(self._full_path(team_id, team_user_id))

        return TeamMembers(**response)

    @staticmethod
    def _full_path(team_id: str, team_user_id: Optional[str] = None) -> str:
        if team_user_id is None:
            return "teams/{team_id}/users".format(team_id=team_id)

        return "teams/{team_id}/users/{team_user_id}".format(team_id=team_id, team_user_id=team_user_id)
