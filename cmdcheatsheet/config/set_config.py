from cmdcheatsheet.configuration import set_config_value
from cmdcheatsheet.models import CommandArgument, CommandDetails
from cmdcheatsheet.validations import validate_configuration


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
