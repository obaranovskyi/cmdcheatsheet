import os
from cmdcheatsheet.models import DefaultConfigurations, DefaultConfig


version = '0.0.17'
user_home_dir = os.path.expanduser('~')

config_dir = f"{user_home_dir}/.config/cmdcheatsheet"
config_name = "config.json"
config_location = f"{config_dir}/{config_name}"

store_name = "commands.json"
default_commands_store_location = f"{config_dir}/{store_name}"

default_config = DefaultConfigurations([
    DefaultConfig(
        "commandsStoreLocation",
        default_commands_store_location,
        'Path to file in JSON format that consists of the command list.'
    ),
    DefaultConfig(
        "alternativeStoreLocations",
        [],
        'Path list to JSON files that might be used as an alternative commands store location.'
    )
])
