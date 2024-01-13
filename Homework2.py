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
        response.raise_for_status()  # Raises HTTPError for bad responses
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error: {e}")
        return {}
    except requests.exceptions.RequestException as e:
        logging.error(f"Request Exception: {e}")
        return {}

    # parse json
    try:
        response_json = response.json()
    except json.JSONDecodeError:
        logging.error("Failed to parse JSON from response")
        return {}

    logging.info("User data retrieved successfully")
    return response_json

# Main execution
if __name__ == "__main__":
    user_obj = get_user_data()

    # Validate and print user data
    if user_obj:
        logging.debug(f"User Object: {user_obj}")
        print('Username:', user_obj.get('login', 'N/A'))
        print('Name:', user_obj.get('name', 'N/A'))
    else:
        logging.warning("No user data to display")
