import os 
from github import Github

# Read GitHub access token from GitHub Secrets
access_token = os.environ.get('GH_TOKEN')
if access_token is None:
    raise ValueError('GitHub access token is not set')

# Create a GitHub instance
g = Github(access_token)

# Get the authenticated user
user = g.get_user()
print(f'Authenticated as {user.login}')
