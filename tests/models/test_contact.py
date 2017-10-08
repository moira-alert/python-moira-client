try:
    from unittest.mock import Mock
    from unittest.mock import patch
except ImportError:
    from mock import Mock
    from mock import patch

from moira_client.client import Client
from moira_client.client import InvalidJSONError
from moira_client.client import ResponseStructureError
from moira_client.models.contact import CONTACT_SLACK
from moira_client.models.contact import Contact
from moira_client.models.contact import ContactManager
from .test_model import ModelTest


class ContactTest(ModelTest):

    def test_add(self):
        client = Client(self.api_url)
        contact_manager = ContactManager(client)

        contact_value = '#channel'
        contact_id = 1

        with patch.object(client, 'put', return_value={'id': contact_id}) as put_mock, \
                patch.object(client, 'get', return_value={'contacts': []}) as get_mock:
            res_contact = contact_manager.add(contact_value, CONTACT_SLACK)

        self.assertTrue(put_mock.called)
        self.assertTrue(get_mock.called)

        expected_request_data = {
            'value': contact_value,
            'type': CONTACT_SLACK
        }

        expected_contact = Contact(id=contact_id, **expected_request_data)

        self.assertEqual(expected_contact, res_contact)

        put_mock.assert_called_with('contact', json=expected_request_data)

    def test_add_bad_response(self):
        client = Client(self.api_url)
        contact_manager = ContactManager(client)

        contact_value = '#channel'

        with patch.object(client, 'put', return_value={}) as put_mock, \
                patch.object(client, 'get', return_value={'contacts': []}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                contact_manager.add(contact_value, CONTACT_SLACK)

        self.assertTrue(put_mock.called)
        self.assertTrue(get_mock.called)
        expected_request_data = {
            'value': contact_value,
            'type': CONTACT_SLACK
        }
        put_mock.assert_called_with('contact', json=expected_request_data)

    def test_fetch_all(self):
        client = Client(self.api_url)
        contact_manager = ContactManager(client)

        with patch.object(client, 'get', return_value={'list': []}) as get_mock:
            contact_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('contact')

    def test_fetch_all_bad_response(self):
        client = Client(self.api_url)
        contact_manager = ContactManager(client)

        with patch.object(client, 'get', return_value={}) as get_mock:
            with self.assertRaises(ResponseStructureError):
                contact_manager.fetch_all()

        self.assertTrue(get_mock.called)
        get_mock.assert_called_with('contact')

    def test_delete(self):
        client = Client(self.api_url)
        contact_manager = ContactManager(client)

        contact_id = '1'

        with patch.object(client, 'delete', new=Mock(side_effect=InvalidJSONError(b''))) as delete_mock:
            res = contact_manager.delete(contact_id)

        self.assertTrue(delete_mock.called)
        self.assertTrue(res)
        delete_mock.assert_called_with('contact/' + contact_id)

    def test_delete_fail(self):
        client = Client(self.api_url)
        contact_manager = ContactManager(client)

        contact_id = '1'

        with patch.object(client, 'delete') as delete_mock:
            res = contact_manager.delete(contact_id)

        self.assertTrue(delete_mock.called)
        self.assertFalse(res)
        delete_mock.assert_called_with('contact/' + contact_id)
