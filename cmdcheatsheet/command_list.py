from rich.prompt import Confirm
from cmdcheatsheet.models import CommandDetails, Command, CommandArgument
from cmdcheatsheet.display import *
from cmdcheatsheet.display_table import *
import cmdcheatsheet.command as command_actions
from cmdcheatsheet.help import help
from cmdcheatsheet.config import *
from cmdcheatsheet.alternative_store import *
from cmdcheatsheet.validations import validate_configuration, is_valid_custom_commands_location
from cmdcheatsheet.messages import show_invalid_store_location_message, show_store_with_name_not_exists
from cmdcheatsheet.logger import yellow, blue, version_details
from cmdcheatsheet.consts import version


class SimpleCommandsList(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands', '-c'],
            'Display all commands.')

    def handler(self, _):
        display_commands()


class SimpleDetailedCommandsList(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands-info', '-ci'],
            'Display all commands, including all details such as ids, etc., all commands.')

    def handler(self, _):
        display_commands(True)
        

class CommandsListTableView(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--commands-table', '-ct'],
            'Display all commands using a table view.')

    def handler(self, _):
        display_table_view()


class AddCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--add', '-a'],
            'Add new command to the list.',
            [CommandArgument('command'), CommandArgument('description')])

    def handler(self, args):
        command = Command(command=args[0], description=args[1])
        command_actions.add_command(command)

    
class UpdateCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--update', '-u'],
            'Update a <command> by id.',
            [CommandArgument('id'), CommandArgument('name'), CommandArgument('description')])

    def handler(self, args):
        command = Command(id=int(args[0]), command=args[1], description=args[2])
        command_actions.update_command(command)


class DeleteCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--delete', '-d'],
            'Delete a <command> by id.',
            [CommandArgument('id')])

    def handler(self, args):
        command_actions.delete_command(int(args[0]))


class SearchCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--find', '-f'],
            'Search for a command.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(args[0])


class DetailedSearchCommand(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--find-info', '-fi'],
            'Search for a command and include all details, such as ids, etc.',
            [CommandArgument('command')])

    def handler(self, args):
        display_command_by_name(args[0], True)


class SearchCommandTableView(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--find-table', '-ft'],
            'Search for a command and show it using a table view.',
            [CommandArgument('command')])

    def handler(self, args):
        display_table_view(command=args[0])


class AvailableCommandNames(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--available-command-names', '-acn'],
            'Show all stored command names.',
            [CommandArgument('number_of_columns', False)])

    def handler(self, args):
        display_command_name_list(int(args[0]) if len(args) > 0 else 5)


class Help(CommandDetails):
    def __init__(self):
       super().__init__(['--help', '-h'], 'Show a program help notes.')

    def handler(self, _):
        help(command_list)

class Version(CommandDetails):
    def __init__(self):
       super().__init__(['--version', '-v'], 'Display version.')

    def handler(self, _):
        version_details(version)

class SetConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--set-config', '-sc'],
            'Set config.',
            [CommandArgument('key'), CommandArgument('value')])

    def handler(self, args):
        key = args[0]
        value = args[1]
        if validate_configuration(key, value):
            set_config_value(key=key, value=value)

class RemoveConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            [ '--remove-config', '-rc'],
            'Remove a config.',
            [CommandArgument('key')])

    def handler(self, args):
        remove_config(key=args[0])

class DisplayConfig(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-configs', '-dc'],
            'Display configurations.',
            [CommandArgument('key', False)])

    def handler(self, args):
        if args:
            display_configurations(args[0])
        else:
            display_configurations()

class DisplayAvailableConfigs(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--display-available-configs', '-dac'],
            'Display available configurations.')

    def handler(self, _):
        display_available_configurations()

class SetConfigToDefault(CommandDetails):
    def __init__(self):
       super().__init__(
            ['--set-config-to-default', '-sctd'],
            'Set the configuration to default.')

    def handler(self, _):
        is_yes = Confirm.ask("Are you sure you want to set your config to default?")
        if is_yes:
            set_config_to_default()

class SetSingleConfigToDefault(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--set-single-config-to-default', '-ssctd'],
        'Set a single configuration to default.',
        [CommandArgument('key')])

    def handler(self, args):
        key = args[0]
        is_yes = Confirm.ask(f"Are you sure you want to set '{key}' to default?")
        if is_yes:
            set_single_config_value_to_default(key)


class AddAlternativeStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--add-alternative-store', '-aas'],
        "Add alternative commands store (JSON file) location.",
        [CommandArgument('store_name'), CommandArgument('store_location')])

    def handler(self, args):
        store_name = args[0]
        store_location = args[1]
        if not is_valid_custom_commands_location(store_location):
            show_invalid_store_location_message()
        elif is_existing_store_name(store_name):
            is_yes = Confirm.ask(
                f"Store with the name '{store_name}' already exists. " +
                "Do you want to override an existing one?")
            if is_yes:
                update_alternative_store(store_name=store_name, store_location=store_location)
        else: 
            add_alternative_store(store_name=store_name, store_location=store_location)


class UpdateAlternativeStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--update-alternative-store', '-uas'],
        "Update alternative commands store (JSON file).",
        [CommandArgument('store_name'), CommandArgument('store_location')])

    def handler(self, args):
        store_name = args[0]
        store_location = args[1]
        if not is_existing_store_name(store_name):
            show_store_with_name_not_exists(store_name)            
        elif not is_valid_custom_commands_location(store_location):
            show_invalid_store_location_message()
        else: 
            update_alternative_store(store_name=store_name, store_location=store_location)

class DeleteAlternativeStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--delete-alternative-store', '-das'] ,
        "Delete alternative commands store (JSON file).",
        [CommandArgument('store_name')])

    def handler(self, args):
        store_name = args[0]
        if is_existing_store_name(store_name):
            delete_alternative_store(store_name=store_name)
        else: 
            show_store_with_name_not_exists(store_name)

class DisplayAvailableAlternativeStores(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--display-available-alternative-stores', '-daas'],
        "Display available alternative stores.")

    def handler(self, _):
        display_alternative_stores()

class SwitchToAlternativeStore(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--switch-to-alternative-store', '-stas'],
        "Switch to alternative store location.",
        [CommandArgument('store_name')])

    def handler(self, args):
        store_name = args[0]
        if is_existing_store_name(store_name):
            is_yes = Confirm.ask(
                "If you switch the location, your config 'commandsStoreLocation' " +
                "will be overridden, and you'll lose its value.\n" +
                "Do you want to proceed?"
            )
            if is_yes:
                switch_to_alternative_store(store_name)
        else: 
            show_store_with_name_not_exists(store_name)

class DisplayAppliedAlternativeStoreName(CommandDetails):
    def __init__(self):
       super().__init__(
        ['--display-applied-alternative-store-name', '-daasn'],
        "Display the name of applied alternative store.")

    def handler(self, _):
        applied_store_name = get_applied_alternative_store_name()
        if applied_store_name: 
            print(f"[{blue}]{applied_store_name}")
        else:
            print(f"[{yellow}]None of the alternative stores were applied.")


command_list = [
    # Display commands
    SimpleCommandsList(),
    SimpleDetailedCommandsList(),
    CommandsListTableView(),

    # Crud commands
    AddCommand(),
    UpdateCommand(),
    DeleteCommand(),

    # Search commands
    SearchCommand(),
    DetailedSearchCommand(),
    SearchCommandTableView(),

    # Global info commands
    AvailableCommandNames(),
    Help(),
    Version(),
    
    # Config commands
    DisplayConfig(),
    DisplayAvailableConfigs(),
    SetConfig(),
    RemoveConfig(),
    SetConfigToDefault(),
    SetSingleConfigToDefault(),
    # Config: Alternative store location 
    AddAlternativeStore(),
    UpdateAlternativeStore(),
    DeleteAlternativeStore(),
    DisplayAvailableAlternativeStores(),
    SwitchToAlternativeStore(),
    DisplayAppliedAlternativeStoreName()
]

def get_command_by_name(command_name):
    return next((c for c in command_list if c.need_to_handle(command_name)), None)

