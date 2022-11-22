from cmdcheatsheet.models import CommandDetails, Command, CommandArgument
from cmdcheatsheet.display import *
from cmdcheatsheet.display_table import *
import cmdcheatsheet.command as command_actions
from cmdcheatsheet.help import help
from cmdcheatsheet.config import *
from rich.prompt import Confirm


class SimpleListCommand(CommandDetails):
    def __init__(self):
       super().__init__(['-p', 'ls'], 'Display all commands.')

    def handler(self, _):
        display_commands()


class SimpleDetailedListCommand(CommandDetails):
    def __init__(self):
       super().__init__(['-i', 'lsi'], 'Display all commands, including all details such as ids, etc., all commands.')

    def handler(self, _):
        display_commands(True)
        

class TableViewCommand(CommandDetails):
    def __init__(self):
       super().__init__(['-t', 'lst'], 'Display all commands using a table view.')

    def handler(self, _):
        display_table_view()


class AddCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-a', '-c'],
            'Add new command to the list.',
            [CommandArgument('command'), CommandArgument('description')])

    def handler(self, args):
        command = Command(command=args[0], description=args[1])
        command_actions.add_command(command)

    
class UpdateCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-u', '-e'],
            'Update a <command> by id.',
            [CommandArgument('id'), CommandArgument('name'), CommandArgument('description')])

    def handler(self, args):
        command = Command(id=int(args[0]), command=args[1], description=args[2])
        command_actions.update_command(command)


class DeleteCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-d', '-r'],
            'Delete a <command> by id.',
            [CommandArgument('id')])

    def handler(self, args):
        command_actions.delete_command(int(args[0]))


class SearchCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-s', '-f'],
            'Search for a command.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(args[0])


class SearchCommandDetailed(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-si', '-fi'],
            'Search for a command and include all details, such as ids, etc.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(args[0], True)


class SearchCommandTableView(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-st', '-ft'],
            'Search for a command and show it using a table view.',
            [CommandArgument('command')])

    def handler(self, args):
        display_table_view(command=args[0])


class NameListCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-nl', 'lsnl'],
            'Show all stored command names.',
            [CommandArgument('number_of_columns', False)])

    def handler(self, args):
        display_command_name_list(int(args[0]) if len(args) > 0 else 5)


class SetConfigCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-sc'],
            'Set config.',
            [CommandArgument('key'), CommandArgument('value')])

    def handler(self, args):
        key = args[0]
        value = args[1]
        if validate_configuration(key, value):
            set_config_value(key=key, value=value)

class RemoveConfigCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-rc'],
            'Remove a config.',
            [CommandArgument('key')])

    def handler(self, args):
        remove_config(key=args[0])

class DisplayConfigCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['-dc'],
            'Display configurations.',
            [CommandArgument('key', False)])

    def handler(self, args):
        if args:
            display_configurations(args[0])
        else:
            display_configurations()

class DisplayAvailableConfigurationsCommand(CommandDetails):
    def __init__(self):
       super().__init__(['-dac'], 'Display available configurations.')

    def handler(self, _):
        display_available_configurations()

class SetConfigToDefaultCommand(CommandDetails):
    def __init__(self):
       super().__init__(['-sctd'], 'Set the configuration to default.')

    def handler(self, _):
        is_yes = Confirm.ask("Are you sure you want to set your config to default?")
        if is_yes:
            set_config_to_default()

class SetSingleConfigToDefaultCommand(CommandDetails):
    def __init__(self):
       super().__init__(
        ['-ssctd'],
        'Set a single configuration to default.',
        [CommandArgument('key')])

    def handler(self, args):
        key = args[0]
        is_yes = Confirm.ask(f"Are you sure you want to set '{key}' to default?")
        if is_yes:
            set_single_config_value_to_default(key)

class HelpCommand(CommandDetails):
    def __init__(self):
       super().__init__(['-h', 'help', '--help'], 'Show a program help notes.')

    def handler(self, _):
        help(command_list)

command_list = [
    # Display commands
    SimpleListCommand(),
    SimpleDetailedListCommand(),
    TableViewCommand(),

    # Crud commands
    AddCommand(),
    UpdateCommand(),
    DeleteCommand(),

    # Search commands
    SearchCommand(),
    SearchCommandDetailed(),
    SearchCommandTableView(),

    # Global info commands
    NameListCommand(),
    HelpCommand(),
    
    # Config commands
    DisplayConfigCommand(),
    DisplayAvailableConfigurationsCommand(),
    SetConfigCommand(),
    RemoveConfigCommand(),
    SetConfigToDefaultCommand(),
    SetSingleConfigToDefaultCommand()
]

def get_command_by_name(command_name):
    return next((c for c in command_list if c.need_to_handle(command_name)), None)

