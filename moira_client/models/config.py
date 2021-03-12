from ..client import ResponseStructureError


class WebContact:
    def __init__(self, _type, label, validation=None, placeholder=None, _help=None):
        self.type = _type
        self.label = label
        self.validation = validation
        self.placeholder = placeholder
        self.help = _help


class Config:
    def __init__(self, remote_allowed, contacts, support_email=None):
        self.remoteAllowed = remote_allowed
        self.contacts = contacts
        self.supportEmail = support_email


class ConfigManager:
    def __init__(self, client):
        self._client = client

    def fetch(self):
        """
        Returns config, see https://moira.readthedocs.io/en/latest/installation/configuration.html

        :return: config

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())

        if 'contacts' not in result:
            raise ResponseStructureError("'contacts' field doesn't exist in response", result)
        if 'remoteAllowed' not in result:
            raise ResponseStructureError("'remoteAllowed' field doesn't exist in response", result)

        contacts = []
        for contact in result['contacts']:
            if self._validate_contact(contact):
                _help = contact['help'] if 'help' in contact else None
                validation = contact['validation'] if 'validation' in contact else None
                placeholder = contact['placeholder'] if 'placeholder' in contact else None
                contacts.append(WebContact(_type=contact['type'], label=contact['label'], validation=validation,
                                           placeholder=placeholder, _help=_help))
        support = result['supportEmail'] if 'supportEmail' in result else None
        return Config(remote_allowed=result['remoteAllowed'], contacts=contacts, support_email=support)

    def _validate_contact(self, contact):
        if 'type' not in contact:
            return False
        if 'label' not in contact:
            return False
        return True

    def _full_path(self, path=''):
        if path:
            return 'config/{}'.format(path)
        return 'config'
