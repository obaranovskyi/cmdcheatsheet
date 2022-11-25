from cmdcheatsheet.alt_store.core import display_alt_stores
from cmdcheatsheet.models import CommandDetails


class DisplayAvailableAltStores(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--display-available-alternative-stores', '-daas'],
        "Display available alternative stores.")

    def handler(self, _):
        display_alt_stores()
