import os
from cmdcheatsheet.models import DefaultConfigurations, DefaultConfig


VERSION = '0.0.19'

USER_HOME_DIR = os.path.expanduser('~')

CONFIG_DIR = f"{USER_HOME_DIR}/.config/cmdcheatsheet"
CONFIG_NAME = "config.json"
CONFIG_LOCATION = f"{CONFIG_DIR}/{CONFIG_NAME}"

STORE_NAME = "commands.json"
DEFAULT_COMMANDS_STORE_LOCATION = f"{CONFIG_DIR}/{STORE_NAME}"

DEFAULT_CONFIG = DefaultConfigurations([
    DefaultConfig(
        "commandsStoreLocation",
        DEFAULT_COMMANDS_STORE_LOCATION,
        'Path to file in JSON format that consists of the command list.'
    ),
    DefaultConfig(
        "alternativeStoreLocations",
        [],
        'Path list to JSON files that might be used as an alternative commands store location.'
    )
])
