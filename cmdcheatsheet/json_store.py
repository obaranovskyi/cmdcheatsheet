import os
import json
from dataclasses import asdict
from cmdcheatsheet.models import Command
from cmdcheatsheet.logger import error

user_home_dir = os.path.expanduser('~')
json_filename = "commands.json"
json_file_dir = f"{user_home_dir}/.config/cmdcheatsheet/{json_filename}"


def setup_config():
    try:
        if not os.path.exists(json_file_dir):
            os.makedirs(os.path.dirname(json_file_dir), exist_ok=True)
            with open(json_file_dir, 'w') as file_object:
                json.dump([], file_object, indent=4)
    except Exception as _:
        error("Error with config creation")

def get_commands():
    setup_config()
    with open(json_file_dir) as f:
      commands = json.load(f)
    return [Command(c.get('command'), c.get('description'), c.get('id')) for c in commands]

def get_index():
    commands = get_commands()
    if not commands:
        return 1
    else:
        last_command = commands[-1]
        return last_command.id + 1

def get_commands_by_includes_command_name(command_name):
    commands = []
    for command in get_commands():
        command_split = command.command.replace(',', '').split(' ')
        if command_name in command_split:
            commands.append(command)
    return commands

def save_all_commands(commands):
    commands_to_save = [asdict(c) for c in commands]
    with open(json_file_dir, 'w') as file_object:
        json.dump(commands_to_save, file_object, indent=4)
