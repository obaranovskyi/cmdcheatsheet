from rich import print
from cmdcheatsheet.shared.logger import BLUE, GREEN


def help_details(command_name, description):
    print(f"[{BLUE}]  {command_name}[{GREEN}] - {description}")
