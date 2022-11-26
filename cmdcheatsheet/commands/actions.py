from cmdcheatsheet.commands.commands import Commands
from cmdcheatsheet.commands.detailed_commands import DetailedCommands
from cmdcheatsheet.commands.table_view_commands import TableViewCommands
from cmdcheatsheet.commands.add_command import AddCommand
from cmdcheatsheet.commands.update_command import UpdateCommand
from cmdcheatsheet.commands.delete_command import DeleteCommand
from cmdcheatsheet.commands.find_command import FindCommand
from cmdcheatsheet.commands.detailed_find_command import DetailedFindCommand
from cmdcheatsheet.commands.table_view_find_command import TableViewFindCommand
from cmdcheatsheet.commands.available_command_names import AvailableCommandNames

command_actions = [
    Commands(),
    DetailedCommands(),
    TableViewCommands(),
    AddCommand(),
    UpdateCommand(),
    DeleteCommand(),
    FindCommand(),
    DetailedFindCommand(),
    TableViewFindCommand(),
    AvailableCommandNames()
]
