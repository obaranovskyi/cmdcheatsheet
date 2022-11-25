from cmdcheatsheet.config.core import read_config
from cmdcheatsheet.config.consts import DEFAULT_CONFIG
from cmdcheatsheet.shared.logger import BLUE, GREEN, error

def display_configurations(key=''): 
    config = read_config()
    if key:
        if key in DEFAULT_CONFIG.configuration_keys():
            config_details(key, config[key])
        else:
            error(f"No configuration found with the name {key}")
    else:
        for key in config:
            config_details(key, config[key])


def display_available_configurations():
    for config in DEFAULT_CONFIG.configs:
        config_details(config.key, config.desc)


def config_details(config_key, config_value):
    if isinstance(config_value, list):
        print(f"[{BLUE}] {config_key}:")
        for config_dict in config_value:
            print(f"[{BLUE}]   {'-'*5}")
            for key in config_dict:
                config_details('  '+key, config_dict.get(key))
    else:
        print(f"[{BLUE}] {config_key}[{GREEN}]: {config_value}")
    
