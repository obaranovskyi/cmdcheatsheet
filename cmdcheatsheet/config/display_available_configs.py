# from cmdcheatsheet.display import display_available_configurations
from cmdcheatsheet.models import CommandDetails


class DisplayAvailableConfigs(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-available-configs', '-dac'],
            'Display available configurations.')

    def handler(self, _):
        pass
        # display_available_configurations()
