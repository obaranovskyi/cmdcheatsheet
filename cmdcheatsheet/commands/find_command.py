from cmdcheatsheet.commands.logger import display_command_by_name
from cmdcheatsheet.models import CommandArgument, CommandDetails


class FindCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--find', '-f'],
            'Search for a command.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(args[0])

