from cmdcheatsheet.command import group_commands_by_name
from cmdcheatsheet.store import get_commands, get_commands_by_includes_command_name
from cmdcheatsheet.logger import error, command_details, config_details, alt_store_details
from cmdcheatsheet.config import read_config, DEFAULT_CONFIG


def display_commands(display_index=False):
    command_dict = group_commands_by_name()
    id_column_size = calc_id_column_size(get_commands())
    for value in command_dict.values():
        for item in value:
            command_details(item, display_index, id_column_size)

def display_command_by_name(command_name, display_index=False):
    commands_to_display = get_commands_by_includes_command_name(command_name)
    if commands_to_display:
        id_column_size = calc_id_column_size(commands_to_display)
        for command in commands_to_display:
           command_details(command, display_index, id_column_size)
    else:
        error("Command not found.")

def calc_id_column_size(commands):
    command_ids = [c.id for c in commands]
    highest_command_id = max(command_ids) if command_ids else ""
    return len(str(highest_command_id))

def display_configurations(key=''): 
    config = read_config()
    if key:
        if key in DEFAULT_CONFIG.configuration_keys():
            config_details(key, config[key])
        else:
            error(f"No configuration found with the name {key}")
    else:
        for key in config:
            config_details(key, config[key])

def display_available_configurations():
    for config in DEFAULT_CONFIG.configs:
        config_details(config.key, config.desc)

def display_alt_store(alt_stores):
    for store in alt_stores:
        alt_store_details(store.get('storeName'), store.get('storeLocation'))

