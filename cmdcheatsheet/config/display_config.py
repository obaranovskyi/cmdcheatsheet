from cmdcheatsheet.config.display import display_config
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class DisplayConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-configs', '-dc'],
            'Display configurations.',
            [CommandArgument('key', False)])

    def handler(self, args):
        if args:
            display_config(args[0])
        else:
            display_config()
