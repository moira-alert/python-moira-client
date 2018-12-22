from requests.auth import HTTPBasicAuth
import requests


class ResponseStructureError(Exception):
    def __init__(self, msg, content):
        """

        :param msg: str error message
        :param content: dict response content
        """
        self.msg = msg
        self.content = content


class InvalidJSONError(Exception):
    def __init__(self, content):
        """

        :param content: bytes response content
        """
        self.content = content


class Client:
    def __init__(self, api_url, auth_custom=None, auth_user=None, auth_pass=None, login=None):
        """

        :param api_url: str Moira API URL
        :param auth_custom: dict auth custom headers
        :param auth_user: str auth user
        :param auth_pass: str auth password
        :param login: str auth login
        """
        if not api_url.endswith('/'):
            self.api_url = api_url + '/'
        else:
            self.api_url = api_url

        self.auth = None
        self.headers = {
            'X-Webauth-User': login,
            'Content-Type': 'application/json',
            'User-Agent': 'Python Moira Client'
            }

        if auth_user and auth_pass:
            self.auth = HTTPBasicAuth(auth_user, auth_pass)

        if auth_custom:
            self.headers.update(auth_custom)

    def get(self, path='', **kwargs):
        """

        :param path: str api path
        :param kwargs: additional parameters for request
        :return: dict response

        :raises: HTTPError
        :raises: InvalidJSONError
        """
        r = requests.get(self._path_join(path), headers=self.headers, auth=self.auth, **kwargs)
        r.raise_for_status()
        try:
            return r.json()
        except ValueError:
            raise InvalidJSONError(r.content)

    def delete(self, path='', **kwargs):
        """

        :param path: str api path
        :param kwargs: additional parameters for request
        :return: dict response

        :raises: HTTPError
        :raises: InvalidJSONError
        """
        r = requests.delete(self._path_join(path), headers=self.headers, auth=self.auth, **kwargs)
        r.raise_for_status()
        try:
            return r.json()
        except ValueError:
            raise InvalidJSONError(r.content)

    def put(self, path='', **kwargs):
        """

        :param path: str api path
        :param kwargs: additional parameters for request
        :return: dict response

        :raises: HTTPError
        :raises: InvalidJSONError
        """
        r = requests.put(self._path_join(path), headers=self.headers, auth=self.auth, **kwargs)
        r.raise_for_status()
        try:
            return r.json()
        except ValueError:
            raise InvalidJSONError(r.content)

    def _path_join(self, *args):
        path = self.api_url
        for part in args:
            path += part
        return path
