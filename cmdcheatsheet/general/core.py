from .consts import HELP_RESPONSIBLE_COMMANDS
from .display import display_help


def help(command_list):
    for c in command_list:
        commands_to_help = []
        for responsible_command in c.responsible_commands:
            command_arguments = [f'<{a.name}{":optional" if not a.required else ""}>' for a in c.command_arguments]
            arguments = (' '  + ' '.join(command_arguments)) if command_arguments else ''
            commands_to_help.append(f'{responsible_command}{arguments}')
        display_help(', '.join(commands_to_help), c.description)

def get_command_by_name(program_actions, command_name):
    return next((c for c in program_actions if c.need_to_handle(command_name)), None)

def is_help_action(command):
    return command in HELP_RESPONSIBLE_COMMANDS
