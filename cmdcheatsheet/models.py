from dataclasses import dataclass
from typing import Any

@dataclass
class DefaultConfig:
    key: str
    value: Any
    desc: str

class DefaultConfigurations:
    def __init__(self, configs=[]):
        self.configs = configs

    def __getitem__(self, config_key):
        return next((c for c in self.configs if c.key == config_key), None)

    def configs_as_dict(self):
        config_dict = dict()
        for config in self.configs:
            config_dict[config.key] = config.value
        return config_dict

    def configuration_keys(self):
        return [config.key for config in self.configs]

@dataclass
class AlternativeStore:
    name: str
    location: str

@dataclass
class Command:
    command: str
    description: str
    id: str = 0

class CommandArgument:
    def __init__(self, name, required=True):
        self.name = name
        self.required = required

class CommandDetails:
    def __init__(self, responsible_commands, description, command_arguments=[]):
        self.responsible_commands = responsible_commands
        self.description = description
        self.command_arguments = command_arguments

    def need_to_handle(self, command):
       return command in self.responsible_commands 

    def handle(self, args=[]):
        error_message = self.validate(args)
        if error_message:
            raise Exception(error_message)
        else:
            self.handler(args)

    def validate(self, args):
        if len(args) < len(self.get_required_command_arguments()):
            return 'Please provide the correct amount arguments.'

        return ""

    def get_required_command_arguments(self):
        return [a for a in self.command_arguments if a.required]

