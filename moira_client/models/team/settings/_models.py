from typing import List

from ...contact import Contact
from ...subscription import Subscription


class TeamSettings:
    def __init__(self, contacts: List[Contact], subscriptions: List[Subscription], team_id: str) -> None:
        self.contacts = contacts
        self.subscriptions = subscriptions
        self.team_id = team_id
