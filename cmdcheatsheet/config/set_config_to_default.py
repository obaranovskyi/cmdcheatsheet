from rich.prompt import Confirm
from cmdcheatsheet.configuration import set_config_to_default
from cmdcheatsheet.models import CommandDetails


class SetConfigToDefault(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--set-config-to-default', '-sctd'],
            'Set the configuration to default.')

    def handler(self, _):
        is_yes = Confirm.ask("Are you sure you want to set your config to default?")
        if is_yes:
            set_config_to_default()
