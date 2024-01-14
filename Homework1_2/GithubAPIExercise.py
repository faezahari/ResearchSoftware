import requests
import matplotlib.pyplot as plt

# Corrected endpoint for searching repositories on GitHub
url = 'https://api.github.com/search/repositories'

# Corrected query parameters
params = {
    'q': 'stars:>1',
    'sort': 'stars',
    'order': 'desc',
    'per_page': 20
}

# Headers including a personal access token for authentication
headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/vnd.github.v3+json'
}

# Make the GET request
r = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if r.status_code == 200:
    # Parse the JSON response
    response_json = r.json()

    # Extract the items (repositories) from the response
    repositories = response_json['items']
    
    # Prepare data for plotting
    repo_names = [repo['full_name'] for repo in repositories]
    stars = [repo['stargazers_count'] for repo in repositories]

    # Create a bar chart
    plt.figure(figsize=(10, 8))
    plt.barh(repo_names, stars, color='skyblue')
    plt.xlabel('Stars')
    plt.title('Top 20 Most Starred Repositories on GitHub')
    plt.gca().invert_yaxis()  # Invert the y-axis to have the repo with the most stars on top
    plt.show()

else:
    print(f"Failed to fetch data: {r.status_code}")