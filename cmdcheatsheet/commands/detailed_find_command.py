from cmdcheatsheet.display import display_command_by_name
from cmdcheatsheet.models import CommandArgument, CommandDetails


class DetailedFindCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--find-info', '-fi'],
            'Search for a command and include all details, such as ids, etc.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(args[0], True)

