from logos.settings.globals import SESSION_FILE

import os
import yaml


def save_session(state):
    """Saves the session state to the session yaml file"""
    state_to_save = {key: value for key, value in state.items()}
    with open(SESSION_FILE, 'w') as file:
        yaml.dump(state_to_save, file)


def load_session():
    """"""


def delete_session(state):
    """"""
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

    for key in list(state.keys()):
        del state[key]
