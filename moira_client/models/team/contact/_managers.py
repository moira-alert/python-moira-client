from ...contact import Contact
from ....client import Client


class TeamContactManager:
    def __init__(self, client: Client) -> None:
        self._client = client

    def create(self, team_id: str, contact: Contact) -> Contact:
        """Create a new team contact"""
        payload = {
            "team_id": team_id,
            "name": contact.name,
            "type": contact.type,
            "value": contact.value,
        }

        response = self._client.post(self._full_path(team_id), json=payload)

        return Contact(**response)

    @staticmethod
    def _full_path(team_id: str) -> str:
        return "teams/{team_id}/contacts".format(team_id=team_id)
