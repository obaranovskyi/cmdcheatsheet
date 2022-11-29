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
class DisplayStrategy:
    config_key: str
    config_value: Any

    def need_to_handle(self, config_key: str) -> bool:
        return self.config_key == config_key

    def display(self) -> None:
        raise NotImplementedError

