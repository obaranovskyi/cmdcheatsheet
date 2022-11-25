#!/bin/python3
import sys

from cmdcheatsheet.shared.logger import error
from cmdcheatsheet.general.core import get_command_by_name, is_help_action
from cmdcheatsheet.config.core import setup_config
from cmdcheatsheet.commands.core import setup_commands_store_config
from cmdcheatsheet.commands.actions import command_actions
from cmdcheatsheet.general.actions import general_actions
from cmdcheatsheet.config.actions import config_actions
from cmdcheatsheet.alt_store.actions import alt_store_actions


def main():
    setup_config()
    setup_commands_store_config()

    if len(sys.argv) == 1:
        sys.argv.append('-c')

    command = sys.argv[1]
    args = sys.argv[2:]

    try:
        program_actions = [
            *command_actions,
            *general_actions,
            *config_actions,
            *alt_store_actions
        ]

        command_to_invoke = get_command_by_name(program_actions, command)
        if command_to_invoke:
            
            if is_help_action(command):
                args.append(program_actions)

            command_to_invoke.handle(args)
        else:
            error("Please provide the valid command name.")

    except Exception as e:
        error(e)

if __name__ == '__main__':
    main()
