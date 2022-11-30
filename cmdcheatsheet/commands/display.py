from rich import print
from rich.console import Console
from rich.table import Table
from .core import *
from cmdcheatsheet.shared.display import *
from .messages import show_command_not_found


def display_command_by_name(query, display_index=False, is_global=False):
    commands_to_display = get_command_by_name(query, is_global)
    if commands_to_display:
        id_column_size = calc_id_column_size(commands_to_display)
        for command in commands_to_display:
            display_find_command(query, command,
                display_index, id_column_size, is_global)
    else:
        show_command_not_found()

def display_command_list(display_index=False):
    command_dict = group_commands_by_name()
    id_column_size = calc_id_column_size(get_commands())
    for value in command_dict.values():
        for item in value:
            display_command(item, display_index, id_column_size)

def display_find_command(query, command, display_index, id_column_length, is_global):
    index_cell = get_index_content(command.id, display_index, id_column_length)
    command_name = highlight_find_results(command.command, query)
    command_description = command.description
    if is_global:
        command_description = highlight_find_results(command.description, query, GREEN)
    print(f"{index_cell}[{BLUE}] {command_name}[{GREEN}] - {command_description}")

def display_command(command, display_index, id_column_length=5):
    index_cell = get_index_content(command.id, display_index, id_column_length)
    print(f"{index_cell}[{BLUE}] {command.command}[{GREEN}] - {command.description}")

def get_index_content(command_id, display_index, id_column_length):
    id = str(command_id) + ' '*(id_column_length - len(str(command_id)))
    return f"[{BLUE}]|[{YELLOW}] {id}[{BLUE}]  |" if display_index else ""

def calc_id_column_size(commands):
    command_ids = [c.id for c in commands]
    highest_command_id = max(command_ids) if command_ids else ""
    return len(str(highest_command_id))

def display_commands_table_view(query=''):
    all_commands = get_command_by_name(query, True) if query else get_commands()
    console = Console()
    table = Table(show_header=True, header_style=RED)
    table.add_column("Id")
    table.add_column("Command")
    table.add_column("Description")
    for c in all_commands:
        command = highlight_find_results(c.command, query)
        description = highlight_find_results(c.description, query, GREEN)
        table.add_row(
            f'[{YELLOW}]{str(c.id)}',
            f'[{BLUE}]{command}',
            f'[{GREEN}]{description}'
        )
    console.print(table)

def display_command_name_list(column_amount):
    commands = get_command_name_list()
    chunked_list = []
    chunk_size = column_amount if len(commands) >= column_amount else len(commands)
    if not chunk_size:
        print(f'[{RED}] No commands have been found yet.')
        return
    for i in range(0, len(commands), chunk_size):
        chunked_list.append(commands[i:i+chunk_size])
    console = Console()
    table = Table(show_header=False, header_style=RED)
    for i in range(chunk_size):
        table.add_column()
    for chunk in chunked_list:
        row = []
        for cn in range(0, chunk_size):
            row.append(f'[{GREEN}]{chunk[cn] if len(chunk) > cn else ""}')
        table.add_row(*row) 
    console.print(table)

