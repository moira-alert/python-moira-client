from ...subscription import SubscriptionModel, Subscription
from ....client import Client


class TeamSubscriptionManager:
    def __init__(self, client: Client) -> None:
        self._client = client

    def create(self, team_id: str, subscription: SubscriptionModel) -> Subscription:
        """Create a new team subscription"""
        payload = {
            "team_id": team_id,
            "contacts": subscription.contacts,
            "tags": subscription.tags,
            "enabled": subscription.enabled,
            "any_tags": subscription.any_tags,
            "throttling": subscription.throttling,
            "sched": subscription.sched,
            "ignore_warnings": subscription.ignore_warnings,
            "ignore_recoverings": subscription.ignore_recoverings,
            "plotting": subscription.plotting,
        }

        response = self._client.post(self._full_path(team_id), json=payload)

        return Subscription(self._client, **response)

    @staticmethod
    def _full_path(team_id: str) -> str:
        return "teams/{team_id}/subscriptions".format(team_id=team_id)
