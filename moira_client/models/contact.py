from ..client import InvalidJSONError
from ..client import ResponseStructureError
from .base import Base

CONTACT_EMAIL = 'mail'
CONTACT_PUSHOVER = 'pushover'
CONTACT_SLACK = 'slack'
CONTACT_TELEGRAM = 'telegram'
CONTACT_TWILIO_SMS = 'twilio sms'
CONTACT_TWILIO_VOICE = 'twilio voice'


class Contact(Base):
    def __init__(self, value='', type='', **kwargs):
        """

        :param value: str contact value
        :param contact_type: str contact type (one of CONTACT_* constants)
        :param kwargs: additional parameters
        """
        self.type = type
        self.value = value
        self.user = kwargs.get('user', None)
        self.name = kwargs.get('name', None)
        self._id = kwargs.get('id', None)


class ContactManager:
    def __init__(self, client):
        self._client = client

    def add(self, value, contact_type, name=None):
        """
        Add new contact

        :param value: str contact value
        :param contact_type: str contact type (one of CONTACT_* constants)
        :param name: str contact name
        :return: Contact

        :raises: ResponseStructureError
        """

        contacts = self.fetch_by_current_user()
        for contact in contacts:
            if contact.value == value and contact.type == contact_type:
                if name and contact.name != name:
                    contact.name = name
                    self.update(contact)
                    return contact
                return contact

        data = {
            'value': value,
            'type': contact_type
        }
        if name:
            data['name'] = name

        result = self._client.put(self._full_path(), json=data)
        if 'id' not in result:
            raise ResponseStructureError('No id in response', result)

        return Contact(id=result['id'], **data)

    def fetch_all(self):
        """
        Returns all existing contacts

        :return: list of Contact

        :raises: ResponseStructureError
        """
        result = self._client.get(self._full_path())
        if 'list' not in result:
            raise ResponseStructureError("list doesn't exist in response", result)

        contacts = []

        for contact in result['list']:
            contacts.append(Contact(**contact))

        return contacts

    def fetch_by_current_user(self):
        """
        Returns all contacts by current user

        :return: list of Contact

        :raises: ResponseStructurteError
        """
        result = self._client.get('user/settings')
        if 'contacts' not in result:
            raise ResponseStructureError("'contacts' field doesn't exist in response", result)

        contacts = []

        for contact in result['contacts']:
            contacts.append(Contact(**contact))

        return contacts

    def get_id(self, type, value):
        """
        Returns contact id by type and value
        Returns None if contact doesn't exist

        :param type: str contact type
        :param value: str contact value
        :return: str contact id
        """
        for contact in self.fetch_all():
            if contact.type == type and contact.value == value:
                return contact.id

    def delete(self, contact_id):
        """
        Delete contact by contact id
        If contact id doesn't exist returns True

        :param contact_id: str contact id
        :return: True if ok, False otherwise

        :raises: ResponseStructureError
        """
        try:
            self._client.delete(self._full_path(contact_id))
            return False
        except InvalidJSONError as e:
            if e.content == b'':  # successfully if response is blank
                return True
            else:
                return False

    def update(self, contact):
        """
        Updates an existing notification contact

        :param contact: Contact
        :return: True if ok, False otherwise
        """
        data = {
            'type': contact.type,
            'value': contact.value,
        }
        if contact.name:
            data['name'] = contact.name

        try:
            self._client.put(self._full_path(contact.id), json=data)
            return True
        except InvalidJSONError:
            return False

    def test(self, contact_id):
        """
        Push a test notification to verify that the contact is properly set up.

        :param contact_id: str contact id
        :return: True if ok, False otherwise
        """

        try:
            self._client.post(self._full_path('{id}/test'.format(id=contact_id)))
            return False
        except InvalidJSONError as e:
            if len(e.content) == 0:  # successfully if response is blank
                return True
            else:
                return False

    def _full_path(self, path=''):
        if path:
            return 'contact/{}'.format(path)
        return 'contact'
