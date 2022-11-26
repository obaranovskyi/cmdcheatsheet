from .display import display_command_list
from cmdcheatsheet.shared.models import CommandDetails


class Commands(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands', '-c'],
            'Display all commands.')

    def handler(self, _):
        display_command_list()

