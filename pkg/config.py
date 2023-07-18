# Main Configuration + Utils Imports
import os
from datetime import datetime

from pkg.utils.color import *
from pkg.utils.local_data import *




# Directories et al
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)).replace("/pkg", "") #root dir for Project
MODELS_DIR = os.path.join(PROJECT_DIR, "models") #artifacts dir for models on local file system
DATA_DIR = os.path.join(PROJECT_DIR, "data")     #local datafiles: {prompts, misc jsons, etc.}
ENVIRONMENT_FILEPATH = os.path.join(PROJECT_DIR, ".env")


# Env Vars
def load_env_file(dotenv_path, override=False):
    """ Taken from- https://stackoverflow.com/questions/40216311/reading-in-environment-variables-from-an-environment-file """
    with open(dotenv_path) as file_obj:
        lines = file_obj.read().splitlines()  # Removes \n from lines

    dotenv_vars = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", maxsplit=1)
        dotenv_vars.setdefault(key, value)

    if override:
        os.environ.update(dotenv_vars)
    else:
        for key, value in dotenv_vars.items():
            os.environ.setdefault(key, value)
    return list(dotenv_vars.keys())


# Hacky method to load in environment variable contents as python vars
# Load in the .env contents + Create named vars in Python Runtime
# keys = load_env_file(ENVIRONMENT_FILEPATH, override=False)
# for key in keys:
    # vars()[key] = os.environ[key] #create a runtime variable mapping each key-->value from the .env
# some_env_var = os.environ["some_env_var"] #above loop avoids having to maintain this for all vars we want to make, linter will not detect because sneaky variable assignment...


