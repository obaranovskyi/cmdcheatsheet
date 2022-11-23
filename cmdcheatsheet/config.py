import os
import json
from rich.prompt import Confirm
from cmdcheatsheet.logger import error
from cmdcheatsheet.json_file import write_json
from cmdcheatsheet.consts import config_location, default_config 


def setup_config():
    if not os.path.exists(config_location):
        os.makedirs(os.path.dirname(config_location), exist_ok=True)
        write_json(config_location, default_config.configs_as_dict())

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

def remove_config(key):
    if key in default_config.configuration_keys():
        is_yes = Confirm.ask(
            f"This config is required. It can't be removed. But it will be set to default. Are you ok?"
        )
        if is_yes:
            set_single_config_value_to_default(key)
        return
    config = read_config()
    if key not in config:
        error("No config was found with such a key.")
    else:
        del config[key]
        write_json(config_location, config)

    
