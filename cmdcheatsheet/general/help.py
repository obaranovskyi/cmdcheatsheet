from .consts import HELP_RESPONSIBLE_COMMANDS
from .core import help as program_help
from cmdcheatsheet.shared.models import CommandDetails


class Help(CommandDetails):
    def __init__(self):
       super().__init__(HELP_RESPONSIBLE_COMMANDS, 'Show a program help notes.')

    def handler(self, args):
        program_help(args[0])

