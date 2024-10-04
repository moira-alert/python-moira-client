from ._models import TeamSettings
from ...contact import Contact
from ...subscription import Subscription
from ....client import Client


class TeamSettingsManager:
    def __init__(self, client: Client) -> None:
        self._client = client

    def get(self, team_id: str) -> TeamSettings:
        """Get team settings"""
        response = self._client.get(self._full_path(team_id))

        return TeamSettings(
            contacts=[Contact(**contact) for contact in response["contacts"]],
            subscriptions=[Subscription(self._client, **subscription) for subscription in response["subscriptions"]],
            team_id=response["team_id"],
        )

    @staticmethod
    def _full_path(team_id: str) -> str:
        return "teams/{team_id}/settings".format(team_id=team_id)
