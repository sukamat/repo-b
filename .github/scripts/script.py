import subprocess

# Command to be executed
# git_command = ['git', 'remote', 'add', '--mirror=fetch', 'repob', 'git@github.com:sukamat/repo-b.git']
git_command = ['git', 'status']

# Output file path
output_file_path = 'output.txt'

# Execute the command and write the result to a text file
with open(output_file_path, 'w') as output_file:
    try:
        subprocess.check_call(git_command, stdout=output_file, stderr=subprocess.STDOUT)
        output_file.write('\nCommand executed successfully!')
    except subprocess.CalledProcessError as e:
        output_file.write(f'\nError: {e}')

print(f'Result has been written to {output_file_path}')