import os
import json
from rich.prompt import Confirm
from cmdcheatsheet.logger import error
from cmdcheatsheet.models import DefaultConfig, DefaultConfigurations


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
    )
])

def setup_app():
   setup_config() 
   setup_commands_store_config()

def setup_config():
    if not os.path.exists(config_location):
        os.makedirs(os.path.dirname(config_location), exist_ok=True)
        write_json(config_location, default_config.configs_as_dict())

def setup_commands_store_config():
    if not os.path.exists(default_commands_store_location):
        write_json(get_store_location(), [])

def read_config():
    with open(config_location) as f:
      config = json.load(f)
    return config

def get_store_location():
    config = read_config()
    return config.get('commandsStoreLocation')

def set_config_value(key, value):
    config = read_config()
    config[key] = value
    write_json(config_location, config)

def set_single_config_value_to_default(key):
    config = read_config()
    config[key] = default_config[key].value
    write_json(config_location, config)

def set_config_to_default():
    os.makedirs(os.path.dirname(config_location), exist_ok=True)
    write_json(config_location, default_config.configs_as_dict())
    
def write_json(file_location, json_content):
    try:
        with open(file_location, 'w') as file_object:
            json.dump(json_content, file_object, indent=4)
    except Exception as _:
        error(f"Can't write to {file_location}")

def validate_configuration(config_name):
    exists = config_name in default_config.configuration_keys()
    valid = True
    if not exists:
        valid = Confirm.ask(
            f"The configuration with the name '{config_name}' doesn't exist." +
            " Therefore, it won't have any impact. Do you still want to add it?"
        )
    return valid
