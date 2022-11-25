from cmdcheatsheet.commands.logger import display_table_view
from cmdcheatsheet.models import CommandDetails


class TableViewCommands(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands-table', '-ct'],
            'Display all commands using a table view.')

    def handler(self, _):
        display_table_view()
