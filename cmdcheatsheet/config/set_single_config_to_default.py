from rich.prompt import Confirm
from .core import set_single_config_value_to_default
from .validators import is_valid_config_key
from cmdcheatsheet.shared.display import display_error
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class SetSingleConfigToDefault(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--set-single-config-to-default', '-ssctd'],
        'Set a single configuration to default.',
        [CommandArgument('key')])

    def handler(self, args):
        key = args[0]
        if not is_valid_config_key(key):
            display_error("This config can't be set to default as it's invalid.")
            return
        is_yes = Confirm.ask(f"Are you sure you want to set '{key}' to default?")
        if is_yes:
            set_single_config_value_to_default(key)

