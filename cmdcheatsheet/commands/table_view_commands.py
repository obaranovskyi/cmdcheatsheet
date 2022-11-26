from .display import display_commands_table_view
from cmdcheatsheet.shared.models import CommandDetails


class TableViewCommands(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands-table', '-ct'],
            'Display all commands using a table view.')

    def handler(self, _):
        display_commands_table_view()
