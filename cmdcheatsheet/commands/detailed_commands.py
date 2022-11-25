from cmdcheatsheet.commands.logger import display_commands
from cmdcheatsheet.models import CommandDetails


class DetailedCommands(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands-info', '-ci'],
            'Display all commands, including all details such as ids, etc., all commands.')

    def handler(self, _):
        display_commands(True)
        

