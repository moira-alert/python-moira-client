import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

import requests
from moira_client.client import Client
from moira_client.client import InvalidJSONError

TEST_API_URL = 'http://test/api/url'
TEST_HEADERS = {
    'X-Webauth-User': 'login',
    'Content-Type': 'application/json',
    'User-Agent': 'Python Moira Client'
    }


class FakeResponse:

    @property
    def content(self):
        return 'not json'

    def raise_for_status(self):
        pass

    def json(self):
        raise ValueError('invalid json')


class ClientTest(unittest.TestCase):

    def test_get(self):

        def get(url, params, **kwargs):
            pass

        with patch.object(requests, 'get', side_effects=get) as mock_get:
            test_path = 'test_path'

            client = Client(TEST_API_URL, TEST_HEADERS)
            client.get(test_path)

        self.assertTrue(mock_get.called)
        expected_url_call = TEST_API_URL + '/' + test_path
        mock_get.assert_called_with(expected_url_call, headers=TEST_HEADERS, auth=None)

    def test_put(self):

        def put(url, data, **kwargs):
            pass

        with patch.object(requests, 'put', side_effects=put) as mock_put:
            test_path = 'test_path'
            test_data = {'test': 'test'}

            client = Client(TEST_API_URL, TEST_HEADERS)
            client.put(test_path, data=test_data)

        self.assertTrue(mock_put.called)
        expected_url_call = TEST_API_URL + '/' + test_path
        mock_put.assert_called_with(expected_url_call, data=test_data, headers=TEST_HEADERS, auth=None)

    def test_delete(self):

        def delete(url, **kwargs):
            pass

        with patch.object(requests, 'delete', side_effects=delete) as mock_delete:
            test_path = 'test_path'

            client = Client(TEST_API_URL, TEST_HEADERS)
            client.delete(test_path)

        self.assertTrue(mock_delete.called)
        expected_url_call = TEST_API_URL + '/' + test_path
        mock_delete.assert_called_with(expected_url_call, headers=TEST_HEADERS, auth=None)

    def test_get_invalid_response(self):

        def get(url, params, **kwargs):
            return FakeResponse()

        response = FakeResponse()

        with patch.object(requests, 'get', side_effects=get, return_value=response) as mock_get:
            test_path = 'test_path'

            client = Client(TEST_API_URL, TEST_HEADERS)
            with self.assertRaises(InvalidJSONError):
                client.get(test_path)

        self.assertTrue(mock_get.called)
        expected_url_call = TEST_API_URL + '/' + test_path
        mock_get.assert_called_with(expected_url_call, headers=TEST_HEADERS, auth=None)

    def test_put_invalid_response(self):
        test_data = {'test': 'test'}

        def put(url, data, **kwargs):
            return FakeResponse()

        response = FakeResponse()

        with patch.object(requests, 'put', side_effects=put, return_value=response) as mock_put:
            test_path = 'test_path'

            client = Client(TEST_API_URL, TEST_HEADERS)
            with self.assertRaises(InvalidJSONError):
                client.put(test_path, data=test_data)

        self.assertTrue(mock_put.called)
        expected_url_call = TEST_API_URL + '/' + test_path
        mock_put.assert_called_with(expected_url_call, data=test_data, headers=TEST_HEADERS, auth=None)

    def test_delete_invalid_response(self):

        def delete(url, **kwargs):
            return FakeResponse()

        response = FakeResponse()

        with patch.object(requests, 'delete', side_effects=delete, return_value=response) as mock_delete:
            test_path = 'test_path'

            client = Client(TEST_API_URL, TEST_HEADERS)
            with self.assertRaises(InvalidJSONError):
                client.delete(test_path)

        self.assertTrue(mock_delete.called)
        expected_url_call = TEST_API_URL + '/' + test_path
        mock_delete.assert_called_with(expected_url_call, headers=TEST_HEADERS, auth=None)
