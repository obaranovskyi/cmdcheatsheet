import json
import os
from dataclasses import asdict
from cmdcheatsheet.config.core import get_store_location
from cmdcheatsheet.config.consts import DEFAULT_COMMANDS_STORE_LOCATION
from cmdcheatsheet.shared.json_file import write_json
from cmdcheatsheet.shared.display import display_info, display_error
from cmdcheatsheet.shared.models import Command


def command_to_name(command):
    command_split = command.split(' ')
    command_name = command_split[1] if command_split[0] == 'sudo' else command_split[0]
    if command_name.endswith(','):
        command_name = command_name.replace(',', '')
    return command_name

def get_command_name_list():
    commands = get_commands()
    command_names = []
    for command in commands:
        command_name = command_to_name(command.command)
        if command_name not in command_names:
            command_names.append(command_name)
    return command_names

def group_commands_by_name():
    commands = get_commands()
    command_dict = {}
    for command in commands:
        command_name = command_to_name(command.command)
        if command_dict.get(command_name) is None:
            command_dict[command_name] = [command]
        else:
            command_dict.get(command_name).append(command)
    return command_dict

def add_command(command): 
    commands = get_commands()
    command_to_add = find_command_by_name(commands, command.command)
    if command_to_add is None:
        command.id = get_index()
        commands.append(command)
        save_commands(commands)
        display_info(f"Command '{command.command}' added.")
        return
    display_info(f"Command '{command.command}' already exists.")

def delete_command(command_id):
    commands = get_commands()
    command_to_delete = find_command_by_id(commands, command_id)
    if command_to_delete is not None:
        commands.remove(command_to_delete)
        save_commands(commands)
        display_info(f"Command with id: {command_id} removed.")
        return
    display_error(f"Command with id: {command_id} not found.")

def update_command(command):
    commands = get_commands()
    command_to_update = find_command_by_id(commands, command.id)
    if command_to_update is not None:
        command_to_update.command = command.command
        command_to_update.description = command.description
        save_commands(commands)
        display_info(f"Command with id: {command.id} updated.")
        return
    display_error(f"Command with id: {command.id} not found.")

def find_command_by_name(commands, command_value):
    return next((c for c in commands if c.command == command_value), None)

def find_command_by_id(commands, id):
    return next((c for c in commands if c.id == id), None)

def get_commands():
    with open(get_store_location()) as f:
      commands = json.load(f)
    return [Command(c.get('command'), c.get('description'), c.get('id')) for c in commands]

def get_index():
    commands = get_commands()
    if not commands:
        return 1
    else:
        last_command = commands[-1]
        return last_command.id + 1

def get_command_by_name(query, is_global):
    commands = get_commands()
    if is_global:
        return [c for c in commands
                if query in c.command or \
                   query in c.description]
    else:
        return [c for c in commands
                if query in c.command.replace(',', '').split(' ')]

def save_commands(commands):
    commands_to_save = [asdict(c) for c in commands]
    write_json(get_store_location(), commands_to_save)

def setup_commands_store_config():
    if not os.path.exists(DEFAULT_COMMANDS_STORE_LOCATION):
        write_json(get_store_location(), [])

