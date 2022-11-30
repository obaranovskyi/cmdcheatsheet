from .display import display_command_by_name 
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class DetailedGlobalFindCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--detailed-global-find', '-gfi'],
            'Search globally for a command and include all details, such as ids, etc.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(query=args[0],
            display_index=True, is_global=True)


