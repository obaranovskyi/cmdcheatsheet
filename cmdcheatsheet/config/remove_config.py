from .core import remove_config
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class RemoveConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            [ '--remove-config', '-rc'],
            'Remove a config.',
            [CommandArgument('key')])

    def handler(self, args):
        remove_config(key=args[0])
