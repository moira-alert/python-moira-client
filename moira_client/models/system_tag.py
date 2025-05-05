from moira_client.client import ResponseStructureError


class SystemTagManager:
    def __init__(self, client) -> None:
        self._client = client
    
    def fetch_all(self):
        """
        Returns all existing system tags

        :return: list of str

        :raises: ResponseStructureError
        """

        result = self._client.get(self._full_path())
        if 'list' not in result:
            raise ResponseStructureError("list doesn't exist in response", result)
        
        return result['list']
    
    def _full_path(self) -> str:
        return 'system-tag'
    
