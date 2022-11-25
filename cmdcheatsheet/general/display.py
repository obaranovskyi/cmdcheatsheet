from rich import print
from cmdcheatsheet.shared.display import BLUE, GREEN


def display_version(current_version):
    print(f"[{BLUE}] Version: [{GREEN}]{current_version}")

def display_help(command_name, description):
    print(f"[{BLUE}]  {command_name}[{GREEN}] - {description}")
