from cmdcheatsheet.alt_store.core import is_existing_store_name, update_alt_store
from cmdcheatsheet.messages import show_invalid_store_location_message, show_store_with_name_not_exists
from cmdcheatsheet.models import AlternativeStore, CommandArgument, CommandDetails
from cmdcheatsheet.validations import is_valid_custom_commands_location


class UpdateAltStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--update-alternative-store', '-uas'],
        "Update alternative commands store (JSON file).",
        [CommandArgument('store_name'), CommandArgument('store_location')])

    def handler(self, args):
        alt_store = AlternativeStore(args[0], args[1])
        if not is_existing_store_name(alt_store.name):
            show_store_with_name_not_exists(alt_store.name)            
        elif not is_valid_custom_commands_location(alt_store.location):
            show_invalid_store_location_message()
        else: 
            update_alt_store(alt_store)
