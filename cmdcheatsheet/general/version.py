from cmdcheatsheet.shared.consts import VERSION
from cmdcheatsheet.general.logger import version_details
from cmdcheatsheet.shared.models import CommandDetails


class Version(CommandDetails):
    def __init__(self):
       super().__init__(['--version', '-v'], 'Display version.')

    def handler(self, _):
        version_details(VERSION)
