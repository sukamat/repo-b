import os 
from github import Github

# Read GitHub access token from GitHub Secrets
access_token = os.environ.get('GH_TOKEN')
print(f'Access token: {access_token}')

temp_var = os.environ.get('TEMP_VAR')
print(f'Temp var: {temp_var}')
