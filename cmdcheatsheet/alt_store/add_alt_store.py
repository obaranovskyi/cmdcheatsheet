from rich.prompt import Confirm
from .core import add_alt_store, is_existing_store_name, update_alt_store
from .models import AlternativeStore
from cmdcheatsheet.shared.messages import show_invalid_store_location_message
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails
from cmdcheatsheet.config.validators import is_valid_custom_commands_location


class AddAltStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--add-alternative-store', '-aas'],
        "Add alternative commands store (JSON file) location.",
        [CommandArgument('store_name'), CommandArgument('store_location')])

    def handler(self, args):
        alt_store = AlternativeStore(args[0], args[1])
        if not is_valid_custom_commands_location(alt_store.location):
            show_invalid_store_location_message()
        elif is_existing_store_name(alt_store.name):
            is_yes = Confirm.ask(
                f"Store with the name '{alt_store.name}' already exists. " +
                "Do you want to override an existing one?")
            if is_yes:
                update_alt_store(alt_store)
        else: 
            add_alt_store(alt_store)

