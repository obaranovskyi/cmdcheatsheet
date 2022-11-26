from rich import print
from .core import get_applied_alt_store_name
from cmdcheatsheet.shared.models import CommandDetails
from cmdcheatsheet.shared.display import YELLOW, BLUE


class DisplayAppliedAltStoreName(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--display-applied-alternative-store-name', '-daasn'],
        "Display the name of applied alternative store.")

    def handler(self, _):
        applied_store_name = get_applied_alt_store_name()
        if applied_store_name: 
            print(f"[{BLUE}]{applied_store_name}")
        else:
            print(f"[{YELLOW}]None of the alternative stores were applied.")
