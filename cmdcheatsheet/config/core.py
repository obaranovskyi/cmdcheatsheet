import os
import json
from rich.prompt import Confirm
from cmdcheatsheet.shared.display import display_error
from cmdcheatsheet.shared.json_file import write_json
from .consts import CONFIG_LOCATION, CURR_STORE_LOCATION_CONF, DEFAULT_CONFIG 


def setup_config():
    if not os.path.exists(CONFIG_LOCATION):
        os.makedirs(os.path.dirname(CONFIG_LOCATION), exist_ok=True)
        write_json(CONFIG_LOCATION, DEFAULT_CONFIG.configs_as_dict())

def read_config():
    with open(CONFIG_LOCATION) as f:
      config = json.load(f)
    return config

def get_store_location():
    config = read_config()
    return config.get(CURR_STORE_LOCATION_CONF)

def set_config_value(key, value):
    config = read_config()
    config[key] = value
    write_json(CONFIG_LOCATION, config)

def set_single_config_value_to_default(key):
    config = read_config()
    config[key] = DEFAULT_CONFIG[key].value
    write_json(CONFIG_LOCATION, config)
  
def set_config_to_default():
    os.makedirs(os.path.dirname(CONFIG_LOCATION), exist_ok=True)
    write_json(CONFIG_LOCATION, DEFAULT_CONFIG.configs_as_dict())

def remove_config(key):
    if key in DEFAULT_CONFIG.configuration_keys():
        is_yes = Confirm.ask(
            f"This config is required. It can't be removed. But it will be set to default. Are you ok?"
        )
        if is_yes:
            set_single_config_value_to_default(key)
        return
    config = read_config()
    if key not in config:
        display_error("No config was found with such a key.")
    else:
        del config[key]
        write_json(CONFIG_LOCATION, config)

