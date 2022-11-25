import os
from cmdcheatsheet.models import DefaultConfigurations, DefaultConfig


VERSION = '0.0.21'

USER_HOME_DIR = os.path.expanduser('~')

CONFIG_DIR = f"{USER_HOME_DIR}/.config/cmdcheatsheet"
CONFIG_NAME = "config.json"
CONFIG_LOCATION = f"{CONFIG_DIR}/{CONFIG_NAME}"

STORE_NAME = "commands.json"
DEFAULT_COMMANDS_STORE_LOCATION = f"{CONFIG_DIR}/{STORE_NAME}"

CURR_STORE_LOCATION_CONF_NAME = 'currentStoreLocation'
ALT_STORES_CONF_NAME = 'alternativeStores'
ALT_STORE_NAME_CONF_NAME = 'storeName'
ALT_STORE_LOCATION_CONF_NAME = 'storeLocation'

DEFAULT_CONFIG = DefaultConfigurations([
    DefaultConfig(
        CURR_STORE_LOCATION_CONF_NAME,
        DEFAULT_COMMANDS_STORE_LOCATION,
        'Path to file in JSON format that consists of the command list.'
    ),
    DefaultConfig(
        ALT_STORES_CONF_NAME,
        [],
        'Path list to JSON files that might be used as an alternative commands store location.'
    )
])

