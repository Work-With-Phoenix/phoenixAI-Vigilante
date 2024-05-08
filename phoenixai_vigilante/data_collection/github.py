import os
import requests

def authenticate_github_api():
    """
    Authenticate with GitHub API using personal access token

    """

 
    github_token = os.getenv('GH_TOKEN') # Load the personal access token from environment variables

    if not github_token:
        raise ValueError("Github token can not be found. Please set the GH_TOKEN environment variable")
    

    headers = {"Authorization":f"token{github_token}"}

def fetch_latest_releases(repo_owner,repo_name, headers):
        """
        Fetches the latest release for a Github repository

        Args:
        - repo_owner: The owner of the repository
        - repo_name: The name of the repository
        - headers: Headers for authenticating with the GitHub API


        Returns:
        - A list of dictionaries representing the latest release
        """


        urls = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases"
        response = requests.get(urls, headers=headers)
        response.raise_for_status # Raise an exception for non-2xx responses


        release = response.json()
        return release
    
    # Authenticate with the GitHub API
headers = authenticate_github_api()


   # List of repositories to collect data from
repositories = {
    "languages": [
        {"owner": "python", "name": "cpython"},
        {"owner": "rust-lang", "name": "rust"},
        {"owner": "nodejs", "name": "node"},
        # Add more language repositories as needed
    ],
    "frameworks": [
        {"owner": "django", "name": "django"},
        {"owner": "rails", "name": "rails"},
        {"owner": "laravel", "name": "laravel"},
        # Add more framework repositories as needed
    ],
    "tools": [
        {"owner": "docker", "name": "docker"},
        {"owner": "kubernetes", "name": "kubernetes"},
        {"owner": "ansible", "name": "ansible"},
        # Add more tool repositories as needed
    ]
}

# Iterate over each category of repositories

for category, repos in repositories.items():
     print(f"Fetching latest release for {category}:")

    #  Iterate over each category in the category 
     for repo in repos:
      repo_owner = repo.owner
      repo_name = repo.name
      latest_releases = fetch_latest_releases(repo_owner, repo_name,headers)
      print(f"Latest Releases for {repo_owner}/{repo_name}:", latest_releases)





    
