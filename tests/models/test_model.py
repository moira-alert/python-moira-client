import unittest


class ModelTest(unittest.TestCase):
    TEST_API_URL = 'http://test/url'

    @property
    def api_url(self):
        return self.TEST_API_URL
