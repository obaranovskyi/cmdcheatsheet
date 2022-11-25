from cmdcheatsheet.consts import VERSION
from cmdcheatsheet.general.logger import version_details
from cmdcheatsheet.models import CommandDetails


class Version(CommandDetails):
    def __init__(self):
       super().__init__(['--version', '-v'], 'Display version.')

    def handler(self, _):
        version_details(VERSION)
