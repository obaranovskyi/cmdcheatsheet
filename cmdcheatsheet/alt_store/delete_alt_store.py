from .core import delete_alt_store, is_existing_store_name
from .messages import show_store_with_name_not_exists
from cmdcheatsheet.shared.models import CommandArgument, CommandDetails


class DeleteAltStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--delete-alternative-store', '-das'] ,
        "Delete alternative commands store (JSON file).",
        [CommandArgument('store_name')])

    def handler(self, args):
        store_name = args[0]
        if is_existing_store_name(store_name):
            delete_alt_store(store_name)
        else: 
            show_store_with_name_not_exists(store_name)
