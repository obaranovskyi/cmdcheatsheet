from cmdcheatsheet.commands.actions import command_actions
from cmdcheatsheet.general.actions import general_actions
from cmdcheatsheet.config.actions import config_actions
# from cmdcheatsheet.alt_store.actions import alt_store_actions
from cmdcheatsheet.models import CommandDetails
from cmdcheatsheet.help import help as program_help

class Help(CommandDetails):
    def __init__(self):
       super().__init__(['--help', '-h'], 'Show a program help notes.')

    def handler(self, _):
        program_help(program_actions)


program_actions = [
    Help(),
    *command_actions,
    *general_actions,
    *config_actions,
    # *alt_store_actions
]

def get_command_by_name(command_name):
    return next((c for c in program_actions if c.need_to_handle(command_name)), None)

