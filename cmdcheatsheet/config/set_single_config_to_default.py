from rich.prompt import Confirm
from cmdcheatsheet.configuration import set_single_config_value_to_default
from cmdcheatsheet.models import CommandArgument, CommandDetails


class SetSingleConfigToDefault(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--set-single-config-to-default', '-ssctd'],
        'Set a single configuration to default.',
        [CommandArgument('key')])

    def handler(self, args):
        key = args[0]
        is_yes = Confirm.ask(f"Are you sure you want to set '{key}' to default?")
        if is_yes:
            set_single_config_value_to_default(key)

