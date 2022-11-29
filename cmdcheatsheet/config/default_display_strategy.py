from rich import print
from .models import DisplayStrategy
from cmdcheatsheet.shared.display import BLUE, GREEN


class DefaultDisplayStrategy(DisplayStrategy):

    def __init__(self, config_key, config_value):
        super().__init__(config_key, config_value)

    def display(self):
        print(f"[{BLUE}]{self.config_key}[{GREEN}]: {self.config_value}")

