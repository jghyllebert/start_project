import os
import virtualenv
from git import Repo

BASE_URL = '/Users/jghyllebert/projects/'


def ask_project_name():
    is_git = raw_input("Do you already have a remote git directory? [Y/N] ")
    if is_git.upper() == "Y":
        is_git = True
        git_url = raw_input("What's the url of this git repository? ")
        git_name = ""  #TODO split git__url, keep only the part before .git
        project_name = raw_input("What's the project's name? [Default: ")
    else:
        is_git = False
        project_name = raw_input("What's the project's name? ")
    directory = raw_input("Where do you want to store this project? [Default: '{}{}/'] ".format(
        BASE_URL,
        project_name
    ))
    if not directory:
        directory = BASE_URL + project_name + "/"
    if os.path.exists(directory):
        directory = raw_input("A directory like this already exists. Where do you want to store it now? ")

    os.makedirs(directory)
    virtualenv.create_environment(directory)
    if is_git:
        Repo.clone_from(git_url, directory + project_name)


