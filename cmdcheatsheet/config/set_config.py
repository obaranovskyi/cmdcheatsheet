from .core import set_config_value
from .validators import validate_configuration
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class SetConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--set-config', '-sc'],
            'Set config.',
            [CommandArgument('key'), CommandArgument('value')])

    def handler(self, args):
        key = args[0]
        value = args[1]
        if validate_configuration(key, value):
            set_config_value(key=key, value=value)
