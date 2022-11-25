# from cmdcheatsheet.display import display_configurations
from cmdcheatsheet.models import CommandArgument, CommandDetails


class DisplayConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-configs', '-dc'],
            'Display configurations.',
            [CommandArgument('key', False)])

    def handler(self, args):
        pass
        # if args:
        #     display_configurations(args[0])
        # else:
        #     display_configurations()
