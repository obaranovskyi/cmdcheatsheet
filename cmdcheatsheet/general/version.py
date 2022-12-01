from .display import display_version
from ..shared.consts import VERSION
from ..shared.models import CommandDetails


class Version(CommandDetails):
    def __init__(self):
       super().__init__(['--version', '-v'], 'Display version.')

    def handler(self, _):
        display_version(VERSION)
