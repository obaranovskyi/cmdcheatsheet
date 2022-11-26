from .display import display_available_configs
from cmdcheatsheet.shared.models import CommandDetails


class DisplayAvailableConfigs(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-available-configs', '-dac'],
            'Display available configurations.')

    def handler(self, _):
        display_available_configs()
