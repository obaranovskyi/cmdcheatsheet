import json
from rich.prompt import Confirm
from .consts import CURR_STORE_LOCATION_CONF, DEFAULT_CONFIG
from cmdcheatsheet.shared.messages import show_invalid_store_location_message


def is_valid_config_key(config_key):
    return config_key in DEFAULT_CONFIG.configuration_keys()

def validate_configuration(config_key, config_value):
    exists = is_valid_config_key(config_key)
    valid = True
    if not exists:
        valid = Confirm.ask(
            f"The configuration with the name '{config_key}' doesn't exist." +
            " Therefore, it won't have any impact. Do you still want to add it?"
        )
    if config_key == CURR_STORE_LOCATION_CONF and not is_valid_custom_commands_location(config_value):
        show_invalid_store_location_message()
        return False
    return valid


def is_valid_custom_commands_location(store_location):
    try:
        with open(store_location) as f:
            commands = json.load(f)
            return isinstance(commands, list)
    except Exception as _: 
        return False
