from rich import print
from rich.console import Console
from rich.table import Table
from cmdcheatsheet.json_store import get_commands, get_commands_by_includes_command_name
from cmdcheatsheet.logger import red, blue, green, yellow
from cmdcheatsheet.command import get_command_name_list


def display_table_view(command=''):
    all_commands = get_commands_by_includes_command_name(command) if command else get_commands()
    console = Console()

    table = Table(show_header=True, header_style=red)

    table.add_column("Id")
    table.add_column("Command")
    table.add_column("Description")

    for c in all_commands:
        table.add_row(
            f'[{yellow}]{str(c.id)}',
            f'[{blue}]{c.command}',
            f'[{green}]{c.description}'
        )

    console.print(table)


def display_command_name_list(column_amount):
    commands = get_command_name_list()
    chunked_list = []

    chunk_size = column_amount if len(commands) >= column_amount else len(commands)

    if not chunk_size:
        print(f'[{red}] No commands have been found yet')
        return

    for i in range(0, len(commands), chunk_size):
        chunked_list.append(commands[i:i+chunk_size])

    console = Console()

    table = Table(show_header=False, header_style=red)

    for i in range(chunk_size):
        table.add_column()

    for chunk in chunked_list:
        row = []
        for cn in range(0, chunk_size):
            row.append(f'[{green}]{chunk[cn] if len(chunk) > cn else ""}')
        table.add_row(*row) 

    console.print(table)
