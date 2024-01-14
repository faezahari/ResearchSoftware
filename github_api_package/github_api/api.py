# api.py
import requests
import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def get_user_data() -> dict:
    """
    Get the authenticated user data object from GitHub.
    Connect to the GitHub API and retrieve the authenticated user's data as a Python dictionary.
    The token is retrieved from an environment variable.

    Returns
    -------
    dict
        User data retrieved from GitHub

    Examples
    --------
    user_obj = get_user_data()
    print(user_obj)

    {
      'name': 'Siti Nurfaezah Binti Zahari',
      'login': 'faezahari',
      ...
    }
    """
    token = os.getenv('DSIAPI')
    
    if not token:
        logging.error("GitHub token not found. Please set the DSIAPI environment variable.")
        return {}

    try:
        response = requests.get(url='https://api.github.com/user', headers={'Authorization': 'Bearer ' + token})
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        response_json = response.json()  # This could raise a JSONDecodeError
    except (requests.exceptions.HTTPError, requests.exceptions.RequestException, json.JSONDecodeError) as e:
        logging.error(f"Error: {e}")
        return {}

    logging.info("User data retrieved successfully")
    return response_json