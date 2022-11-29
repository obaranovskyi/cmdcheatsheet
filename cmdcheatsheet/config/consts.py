import os
from .models import DefaultConfigurations, DefaultConfig

USER_HOME_DIR = os.path.expanduser('~')

CONFIG_DIR = f"{USER_HOME_DIR}/.config/cmdcheatsheet"
CONFIG_NAME = "config.json"
CONFIG_LOCATION = f"{CONFIG_DIR}/{CONFIG_NAME}"

STORE_NAME = "commands.json"
DEFAULT_COMMANDS_STORE_LOCATION = f"{CONFIG_DIR}/{STORE_NAME}"

# Config property names
CURR_STORE_LOCATION_CONF = 'currentStoreLocation'
ALT_STORES_CONF = 'alternativeStores'
ALT_STORE_NAME_CONF = 'storeName'
ALT_STORE_LOCATION_CONF = 'storeLocation'

DEFAULT_CONFIG = DefaultConfigurations([
    DefaultConfig(
        CURR_STORE_LOCATION_CONF,
        DEFAULT_COMMANDS_STORE_LOCATION,
        'Path to file in JSON format that consists of the command list.'
    ),
    DefaultConfig(
        ALT_STORES_CONF,
        [],
        'Path list to JSON files that might be used as an alternative commands store location.'
    )
])


