from .commands import Commands
from .detailed_commands import DetailedCommands
from .table_view_commands import TableViewCommands
from .add_command import AddCommand
from .update_command import UpdateCommand
from .delete_command import DeleteCommand
from .find_command import FindCommand
from .detailed_find_command import DetailedFindCommand
from .table_view_find_command import TableViewFindCommand
from .available_command_names import AvailableCommandNames

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
