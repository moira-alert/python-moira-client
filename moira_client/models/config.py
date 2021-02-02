from ..client import ResponseStructureError


class WebContact:
    def __init__(self, _type: str, label: str, **kwargs):
        self.type = _type
        self.label = label
        self.validation = kwargs.get('validation', None)
        self.placeholder = kwargs.get('placeholder', None)
        self.help = kwargs.get('help', None)


class Config:
    def __init__(self, remote_allowed: bool, contacts: WebContact, **kwargs):
        self.remoteAllowed = remote_allowed
        self.contacts = contacts
        self.supportEmail = kwargs.get('supportEmail', None)


class ConfigManager:
    def __init__(self, client):
        self._client = client

    def fetch(self):
        """
        Returns config, see https://moira.readthedocs.io/en/latest/installation/configuration.html

        :return: config

        """
        result = self._client.get(self._full_path())

        if 'contacts' not in result:
            raise ResponseStructureError("'contacts' field doesn't exist in response", result)
        if 'remoteAllowed' not in result:
            raise ResponseStructureError("'remoteAllowed' field doesn't exist in response", result)

        contacts = []
        for contact in result['contacts']:
            if self._validate_contact(contact):
                contacts.append(WebContact(_type=contact['type'], **contact))
        result['contacts'] = contacts
        return Config(result['remoteAllowed'], **result)

    def _validate_contact(self, contact):
        if 'type' not in contact:
            return False
        if 'label' not in contact:
            return False
        return True

    def _full_path(self, path=''):
        if path:
            return 'config/' + path
        return 'config'
