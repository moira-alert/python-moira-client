from ..base import Base
from typing import List


class TeamModel(Base):
    def __init__(self, description: str, name: str, **kwargs):
        self.description = description
        self.name = name
        self._id = kwargs.get("id", None)


class UserTeams:
    def __init__(self, teams: List[TeamModel]):
        self.teams = teams


class SaveTeamResponse(Base):
    def __init__(self, **kwargs):
        self._id = kwargs.get("id")
