from rich.prompt import Confirm
from .core import is_existing_store_name, switch_to_alt_store
from .messages import show_store_with_name_not_exists
from cmdcheatsheet.config.consts import CURR_STORE_LOCATION_CONF
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class SwitchToAltStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--switch-to-alternative-store', '-stas'],
        "Switch to alternative store location.",
        [CommandArgument('store_name')])

    def handler(self, args):
        store_name = args[0]
        if is_existing_store_name(store_name):
            is_yes = Confirm.ask(
                f"If you switch the location, your config '{CURR_STORE_LOCATION_CONF}' " +
                "will be overridden, and you'll lose its value.\n" +
                "Do you want to proceed?"
            )
            if is_yes:
                switch_to_alt_store(store_name)
        else: 
            show_store_with_name_not_exists(store_name)
