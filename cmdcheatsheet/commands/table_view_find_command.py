from .display import display_commands_table_view
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class TableViewFindCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--find-table', '-ft'],
            'Search for a command and show it using a table view.',
            [CommandArgument('command')])

    def handler(self, args):
        display_commands_table_view(query=args[0])

