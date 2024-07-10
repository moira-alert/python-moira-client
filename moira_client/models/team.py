from requests import HTTPError

from ..client import InvalidJSONError
from ..client import ResponseStructureError
from .base import Base


class Team(Base):
    def __init__(self, name='', description='', **kwargs):
        """

        :param name: str team name
        :param description: str team description
        :param kwargs: additional parameters
        """
        self.name = name
        self.description = description
        self._id = kwargs.get('id', None)


def _full_path(path=''):
    if path:
        return 'teams/{}'.format(path)
    return 'teams'


class TeamManager:
    def __init__(self, client):
        self._client = client

    def get_my_all_teams(self):
        """
        Get all team

        :return: list of Team
        """
        response = self._client.get(_full_path())
        teams = []
        for team in response['teams']:
            teams.append(Team(**team))

        return teams

    def create(self, team_name, team_description):
        """
        Create team

        :param team_name: str team name
        :param team_description: str team description
        :return: Team
        """
        payload = {
            "name": team_name,
            "description": team_description
        }
        try:
            result = self._client.post(_full_path(), json=payload)
            return Team(**result)
        except InvalidJSONError:
            return result

    ## не работает
    def patch(self, team_id, team):
        payload = {
            "name": team.name,
            "description": team.description
        }

        try:
            self._client.patch(_full_path(team_id), json=payload)
            return True
        except InvalidJSONError:
            return False

    def get(self, team_id):
        """
        Get team

        :param team_id: str team id
        :return: Team
        """
        response = self._client.get(_full_path(team_id))
        return response

    def get_settings(self, team_id):
        response = self._client.get(_full_path('{team_id}/settings'.format(team_id=team_id)))
        return response

    def get_users(self, team_id):
        response = self._client.get(_full_path('{team_id}/users'.format(team_id=team_id)))
        return response

    def delete(self, team_id):
        """
        Delete team

        :param team_id: str team id
        :return: True if deleted, False otherwise
        """
        try:
            self._client.delete(_full_path(team_id))
            return True
        except (InvalidJSONError, HTTPError):
            return False
        
    def post_users(self, team_id, usernames):
        payload = {
            "usernames": usernames,
        }

        result = self._client.post(_full_path('{team_id}/users'.format(team_id=team_id)), json=payload)
        return result
    
    def patch_users(self, team_id, usernames):
        payload = {
            "usernames": usernames,
        }

        result = self._client.patch(_full_path('{team_id}/users'.format(team_id=team_id)), json=payload)
        return result 
    
    def delete_user(self, team_id, username):
        try:
            self._client.delete(_full_path('{team_id}/users/{username}'.format(team_id=team_id)))
            return True
        except (InvalidJSONError, HTTPError):
            return False  
