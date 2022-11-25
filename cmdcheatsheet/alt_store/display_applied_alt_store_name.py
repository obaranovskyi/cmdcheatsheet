from cmdcheatsheet.alt_store_core import get_applied_alt_store_name
from cmdcheatsheet.models import CommandDetails
from cmdcheatsheet.logger import yellow, blue


class DisplayAppliedAltStoreName(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--display-applied-alternative-store-name', '-daasn'],
        "Display the name of applied alternative store.")

    def handler(self, _):
        applied_store_name = get_applied_alt_store_name()
        if applied_store_name: 
            print(f"[{blue}]{applied_store_name}")
        else:
            print(f"[{yellow}]None of the alternative stores were applied.")
