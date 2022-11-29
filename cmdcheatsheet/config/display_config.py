from .display import display_configs
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class DisplayConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-configs', '-dc'],
            'Display configurations.',
            [CommandArgument('key', False)])

    def handler(self, args):
        if args:
            display_configs(args[0])
        else:
            display_configs()
