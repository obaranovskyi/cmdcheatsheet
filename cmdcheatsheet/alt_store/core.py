from .display import display_alt_store_list
from cmdcheatsheet.config.core import read_config, set_config_value
from cmdcheatsheet.shared.json_file import write_json
from cmdcheatsheet.config.consts import *


def add_alt_store(alt_store):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF)
    alt_store_to_add = dict()
    alt_store_to_add[ALT_STORE_NAME_CONF] = alt_store.name
    alt_store_to_add[ALT_STORE_LOCATION_CONF] = alt_store.location
    alt_stores.append(alt_store_to_add)
    write_json(CONFIG_LOCATION, config)
    
def update_alt_store(alt_store_to_update):
    config = read_config()
    for alt_store in config.get(ALT_STORES_CONF) :
        if alt_store.get(ALT_STORE_NAME_CONF) == alt_store_to_update.name:
            alt_store[ALT_STORE_LOCATION_CONF] = alt_store_to_update.location
    write_json(CONFIG_LOCATION, config)

def delete_alt_store(store_name):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF)
    config[ALT_STORES_CONF] = exclude_by_name_filter(alt_stores, store_name)
    write_json(CONFIG_LOCATION, config)

def is_existing_store_name(store_name):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF)
    alt_store_names = [store.get(ALT_STORE_NAME_CONF) for store in alt_stores]
    return store_name in alt_store_names

def exclude_by_name_filter(alt_stores, store_name):
    return [store for store in alt_stores if store.get(ALT_STORE_NAME_CONF) != store_name]

def display_alt_stores():
    display_alt_store_list(read_config().get(ALT_STORES_CONF))

def find_alt_store_by_name(store_name):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF)
    return next((s for s in alt_stores if s.get(ALT_STORE_NAME_CONF) == store_name), None)

def switch_to_alt_store(store_name):
    alt_store = find_alt_store_by_name(store_name)
    store_location = alt_store.get(ALT_STORE_LOCATION_CONF)
    set_config_value(CURR_STORE_LOCATION_CONF, store_location)

def get_applied_alt_store_name():
    alt_store_name = None
    config = read_config()
    commands_store_location = config.get(CURR_STORE_LOCATION_CONF)
    alt_stores = config.get(ALT_STORES_CONF)
    for store in alt_stores:
        if store.get(ALT_STORE_LOCATION_CONF) == commands_store_location:
            alt_store_name = store.get(ALT_STORE_NAME_CONF)
    return alt_store_name if alt_store_name else ''

