import os 
from github import Github

# Read GitHub access token from GitHub Secrets
access_token = os.environ.get('GH_TOKEN')
print(f'Access token: {access_token}')

