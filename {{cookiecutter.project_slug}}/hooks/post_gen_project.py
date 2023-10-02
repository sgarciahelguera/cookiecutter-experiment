import re
import sys
import subprocess

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'

if not re.match(r'^[-._a-zA-Z0-9]+$', REPO_NAME):
    print(f'ERROR: {REPO_NAME} is not a valid Python module name!')
    sys.exit(1)

if VISIBILITY not in ["public", "private", "internal"]:
    print(f'ERROR: {VISIBILITY} is not a valid visibility for github, it must be one of "public", "private" or "internal"')
    sys.exit(1)

subprocess.call(["git", "init", "-b", "main"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "first commit"])

gh_cli_command = [
    "gh", "repo", "create",
    f"{REPO_NAME}",
    "--source=.",
    f"--{VISIBILITY}",
    "--push",
    f"--description={DESCRIPTION}",
]
subprocess.call(gh_cli_command)