from rich import print
from cmdcheatsheet.shared.logger import BLUE, GREEN


def version_details(current_version):
    print(f"[{BLUE}] Version: [{GREEN}]{current_version}")

def help_details(command_name, description):
    print(f"[{BLUE}]  {command_name}[{GREEN}] - {description}")
