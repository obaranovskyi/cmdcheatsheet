from rich import print
from .alt_store_display_strategy import AltStoreDisplayStrategy
from .default_display_strategy import DefaultDisplayStrategy
from .core import read_config
from .consts import DEFAULT_CONFIG, CURR_STORE_LOCATION_CONF
from cmdcheatsheet.shared.display import BLUE, GREEN, display_error

DISPLAY_STRATEGIES = [
    DefaultDisplayStrategy(
        CURR_STORE_LOCATION_CONF,
        read_config().get(CURR_STORE_LOCATION_CONF)
    ),
    AltStoreDisplayStrategy()
]

def find_display_handler(config_key):
    return next(
        (ds for ds in DISPLAY_STRATEGIES if ds.need_to_handle(config_key)),
        None)

def display_configs(key=''): 
    if key:
        if key in DEFAULT_CONFIG.configuration_keys():
            display_single_config(key)
        else:
            display_error(f"No configuration found with the name {key}")
    else:
        config = read_config()
        for key in config:
            display_single_config(key)

def display_available_configs():
    for config in DEFAULT_CONFIG.configs:
        print(f"[{BLUE}]{config.key}[{GREEN}]: {config.desc}")

def display_single_config(config_key):
    handler = find_display_handler(config_key)
    handler.display()

