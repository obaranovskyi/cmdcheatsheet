from rich import print
from cmdcheatsheet.config.core import read_config
from cmdcheatsheet.config.consts import DEFAULT_CONFIG
from cmdcheatsheet.shared.display import BLUE, GREEN, display_error

def display_config(key=''): 
    config = read_config()
    if key:
        if key in DEFAULT_CONFIG.configuration_keys():
            display_configs(key, config[key])
        else:
            display_error(f"No configuration found with the name {key}")
    else:
        for key in config:
            display_configs(key, config[key])

def display_available_configs():
    for config in DEFAULT_CONFIG.configs:
        display_configs(config.key, config.desc)

def display_configs(config_key, config_value):
    if isinstance(config_value, list):
        print(f"[{BLUE}] {config_key}:")
        for config_dict in config_value:
            print(f"[{BLUE}]   {'-'*5}")
            for key in config_dict:
                display_configs('  '+key, config_dict.get(key))
    else:
        print(f"[{BLUE}] {config_key}[{GREEN}]: {config_value}")
    
