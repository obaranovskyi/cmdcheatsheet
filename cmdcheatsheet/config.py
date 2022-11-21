import os
import json
from cmdcheatsheet.logger import error


user_home_dir = os.path.expanduser('~')

config_dir = f"{user_home_dir}/.config/cmdcheatsheet"
config_name = "config.json"
config_location = f"{config_dir}/{config_name}"

store_name = "commands.json"
default_commands_store_location = f"{config_dir}/{store_name}"

default_config = {
    "commandsStoreLocation": default_commands_store_location
}

def setup_app():
   setup_config() 
   setup_commands_store_config()

def setup_config():
    if not os.path.exists(config_location):
        os.makedirs(os.path.dirname(config_location), exist_ok=True)
        write_json(config_location, default_config)

def setup_commands_store_config():
    if not os.path.exists(default_commands_store_location):
        write_json(get_store_location(), [])

def read_config():
    with open(config_location) as f:
      config = json.load(f)
    return config

def get_store_location():
    config = read_config()
    return config.get('commandsStoreLocation', default_commands_store_location)

def set_config_value(key, value):
    config = read_config()
    config[key] = value
    write_json(config_location, config)
    
def write_json(file_location, json_content):
    try:
        with open(file_location, 'w') as file_object:
            json.dump(json_content, file_object, indent=4)
    except Exception as _:
        error(f"Can't write to {file_location}")
