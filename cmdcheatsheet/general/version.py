from .display import display_version
from cmdcheatsheet.shared.consts import VERSION
from cmdcheatsheet.shared.models import CommandDetails


class Version(CommandDetails):
    def __init__(self):
       super().__init__(['--version', '-v'], 'Display version.')

    def handler(self, _):
        display_version(VERSION)
