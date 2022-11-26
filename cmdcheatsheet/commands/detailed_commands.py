from .display import display_command_list
from cmdcheatsheet.shared.models import CommandDetails


class DetailedCommands(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands-info', '-ci'],
            'Display all commands, including all details such as ids, etc., all commands.')

    def handler(self, _):
        display_command_list(True)
        

