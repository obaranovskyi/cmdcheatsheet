from rich import print


blue = "turquoise2"
red = "deep_pink2"
green = "spring_green1"
yellow = "yellow"

def info(message):
    print(f"[{blue}]{message}")

def error(message):
    print(f"[{red}]{message}")

def command_details(command, display_index, id_column_length=5):
    id = str(command.id) + ' '*(id_column_length - len(str(command.id)))
    index = f"[{blue}]|[{yellow}] {id}[{blue}]  |" if display_index else ""
    print(f"{index}[{blue}] {command.command}[{green}] - {command.description}")

def help_details(command_name, description):
    print(f"[{blue}]  {command_name}[{green}] - {description}")

