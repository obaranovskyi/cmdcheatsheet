import os
import json
from dataclasses import asdict
from cmdcheatsheet.models import Command
from cmdcheatsheet.config import get_store_location
from cmdcheatsheet.json_file import write_json
from cmdcheatsheet.consts import default_commands_store_location


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

def get_commands_by_includes_command_name(command_name):
    commands = []
    for command in get_commands():
        command_split = command.command.replace(',', '').split(' ')
        if command_name in command_split:
            commands.append(command)
    return commands

def save_all_commands(commands):
    commands_to_save = [asdict(c) for c in commands]
    write_json(get_store_location(), commands_to_save)

def setup_commands_store_config():
    if not os.path.exists(default_commands_store_location):
        write_json(get_store_location(), [])

