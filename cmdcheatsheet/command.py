from cmdcheatsheet.json_store import get_commands, save_all_commands, get_index
from cmdcheatsheet.logger import info, error


# TODO: this and `group_commands_by_name` might be both refactored
# as they use too much the same code
def get_command_name_list():
    commands = get_commands()
    command_names = []

    for command in commands:
        command_split = command.command.split(' ')
        command_name = command_split[1] if command_split[0] == 'sudo' else command_split[0]

        if command_name.endswith(','):
            command_name = command_name.replace(',', '')

        if command_name not in command_names:
            command_names.append(command_name)

    return command_names


def group_commands_by_name():
    commands = get_commands()
    command_dict = {}

    for command in commands:
        command_split = command.command.split(' ')
        command_name = command_split[1] if command_split[0] == 'sudo' else command_split[0]

        if command_name.endswith(','):
            command_name = command_name.replace(',', '')

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
        save_all_commands(commands)
        info(f"Command \"{command.command}\" added.")
        return

    info(f"Command \"{command.command}\" already exists.")


def delete_command(command_id):
    commands = get_commands()
    command_to_delete = find_command_by_id(commands, command_id)

    if command_to_delete is not None:
        commands.remove(command_to_delete)
        save_all_commands(commands)
        info(f"Command with id: {command_id} removed.")
        return

    error(f"Command with id: {command_id} not found.")


def find_command_by_name(commands, command_value):
    return next((c for c in commands if c.command == command_value), None)


def find_command_by_id(commands, id):
    return next((c for c in commands if c.id == id), None)


def update_command(command):
    commands = get_commands()
    command_to_update = find_command_by_id(commands, command.id)

    if command_to_update is not None:
        command_to_update.command = command.command
        command_to_update.description = command.description
        save_all_commands(commands)
        info(f"Command with id: {command.id} updated.")
        return

    error(f"Command with id: {command.id} not found.")
