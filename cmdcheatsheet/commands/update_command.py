from .core import update_command
from cmdcheatsheet.shared.models import Command, CommandArgument, CommandDetails


class UpdateCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--update', '-u'],
            'Update a <command> by id.',
            [CommandArgument('id'), CommandArgument('name'), CommandArgument('description')])

    def handler(self, args):
        command = Command(id=int(args[0]), command=args[1], description=args[2])
        update_command(command)

