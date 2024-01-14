import unittest
from unittest.mock import patch, Mock
import requests
import json
from github_api import api

class TestGitHubApi(unittest.TestCase):

    @patch('github_api.api.os.getenv', return_value='dummy_token')
    @patch('github_api.api.requests.get')
    def test_get_user_data_bad_response(self, mock_get, mock_getenv):
        # Mock successful response
        mock_response = Mock()
        mock_response.json.side_effect = json.JSONDecodeError("Expecting value", "", 0)  # Simulate bad JSON
        mock_get.return_value = mock_response
        result = api.get_user_data()
        self.assertEqual(result, {})  # Check that an empty dict is returned

        # Call the function
        result = api.get_user_data()

        # Asserts
        self.assertEqual(result['login'], 'testuser')
        self.assertEqual(result['name'], 'Test User')

    @patch('github_api.api.os.getenv', return_value='dummy_token')
    @patch('github_api.api.requests.get')
    def test_get_user_data_failure(self, mock_get, mock_getenv):
        # Mock HTTP error
        mock_get.side_effect = requests.exceptions.HTTPError()  # Simulate HTTP error
        result = api.get_user_data()
        self.assertEqual(result, {})  # Check that an empty dict is returned

    @patch('github_api.api.os.getenv', return_value='dummy_token')
    @patch('github_api.api.requests.get')
    def test_get_user_data_bad_response(self, mock_get, mock_getenv):
        # Mock bad JSON response
        mock_response = Mock()
        mock_response.json.side_effect = ValueError("No JSON object could be decoded")
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the function
        result = api.get_user_data()

        # Asserts
        self.assertEqual(result, {})

    # ... any additional tests ...

if __name__ == '__main__':
    unittest.main()