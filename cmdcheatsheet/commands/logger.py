from cmdcheatsheet.shared.logger import BLUE, GREEN, YELLOW


def command_details(command, display_index, id_column_length=5):
    id = str(command.id) + ' '*(id_column_length - len(str(command.id)))
    index = f"[{BLUE}]|[{YELLOW}] {id}[{BLUE}]  |" if display_index else ""
    print(f"{index}[{BLUE}] {command.command}[{GREEN}] - {command.description}")

