from .core import add_command
from ..shared.models import Command, CommandArgument, CommandDetails


class AddCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--add', '-a'],
            'Add new command to the list.',
            [CommandArgument('command'), CommandArgument('description')])

    def handler(self, args):
        command = Command(command=args[0], description=args[1])
        add_command(command)

