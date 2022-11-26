from .core import delete_command
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class DeleteCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--delete', '-d'],
            'Delete a <command> by id.',
            [CommandArgument('id')])

    def handler(self, args):
        delete_command(int(args[0]))
