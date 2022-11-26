from .display import display_command_name_list
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class AvailableCommandNames(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--available-command-names', '-acn'],
            'Show all stored command names.',
            [CommandArgument('number_of_columns', False)])

    def handler(self, args):
        display_command_name_list(int(args[0]) if len(args) > 0 else 5)
