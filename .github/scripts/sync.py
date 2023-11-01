import os 
from github import Github

# Repository names
source_repo_name = 'repo-a'
destination_repo_name = 'repo-b'
organization_name = 'sukamat'

# Read GitHub access token from GitHub Secrets
access_token = os.environ.get('GH_TOKEN')
if access_token is None:
    raise ValueError('GitHub access token is not set')

# Create a GitHub instance
g = Github(access_token)

# Get the authenticated user
user = g.get_user()
print(f'Authenticated as {user.login}')

# Get source and destination repositories
source_repo = g.get_repo(f'{organization_name}/{source_repo_name}')
destination_repo = g.get_repo(f'{organization_name}/{destination_repo_name}')

# Get branches of the repositories
source_default_branch = source_repo.default_branch
destination_default_branch = destination_repo.default_branch

# Get commits of the default branches in both repositories
source_commits = set(commit.sha for commit in source_repo.get_commits(source_default_branch))
destination_commits = set(commit.sha for commit in destination_repo.get_commits(destination_default_branch))

# Find the difference between the two repositories
new_commits = source_commits - destination_commits

if new_commits:
    # Create a pull request in the destination repository
    title = 'Update from Repo-A'
    body = 'Automatically generated pull request to merge changes from Repo-A.'
    try:
        pull_request = destination_repo.create_pull(
            title=title,
            body=body,
            head=source_default_branch,
            base=destination_default_branch
        )
        print(f'Pull request created: {pull_request.html_url}')
    except Exception as e:
        print(f'Error creating pull request: {e}')
else:
    print('No new changes to merge.')
