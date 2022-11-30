from .display import display_command_by_name 
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class GlobalFindCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--global-find', '-gf'],
            'Global search.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(query=args[0], is_global=True)


