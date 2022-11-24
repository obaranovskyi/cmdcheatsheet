from cmdcheatsheet.config import read_config, set_config_value
from cmdcheatsheet.json_file import write_json
from cmdcheatsheet.consts import ALT_STORE_LOCATION_CONF_NAME, ALT_STORE_NAME_CONF_NAME, ALT_STORES_CONF_NAME, CONFIG_LOCATION, CURR_STORE_LOCATION_CONF_NAME
from cmdcheatsheet.display import display_alt_store


def add_alt_store(alt_store):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF_NAME)
    alt_stores.append({
        [ALT_STORE_NAME_CONF_NAME]: alt_store.name,
        [ALT_STORE_LOCATION_CONF_NAME]: alt_store.location 
    })
    write_json(CONFIG_LOCATION, config)
    
def update_alt_store(alt_store_to_update):
    config = read_config()
    for alt_store in config.get(ALT_STORES_CONF_NAME) :
        if alt_store.get(ALT_STORE_NAME_CONF_NAME) == alt_store_to_update.name:
            alt_store[ALT_STORE_LOCATION_CONF_NAME] = alt_store_to_update.location
    write_json(CONFIG_LOCATION, config)

def delete_alt_store(store_name):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF_NAME)
    config[ALT_STORES_CONF_NAME] = exclude_by_name_filter(alt_stores, store_name)
    write_json(CONFIG_LOCATION, config)

def is_existing_store_name(store_name):
    config = read_config()
    alt_stores = config.get(ALT_STORES_CONF_NAME)
    alt_store_names = [store.get(ALT_STORE_NAME_CONF_NAME) for store in alt_stores]
    return store_name in alt_store_names

def exclude_by_name_filter(alt_stores, store_name):
    return [store for store in alt_stores if store.get(ALT_STORE_NAME_CONF_NAME) != store_name]

def display_alt_stores():
    display_alt_store(read_config().get(ALT_STORES_CONF_NAME))

def find_alt_store_by_name(store_name):
    config = read_config()
    return next((store for store in config.get(ALT_STORES_CONF_NAME) if store.get(ALT_STORE_NAME_CONF_NAME) == store_name), None)

def switch_to_alt_store(store_name):
    alt_store = find_alt_store_by_name(store_name)
    store_location = alt_store.get(ALT_STORE_LOCATION_CONF_NAME)
    set_config_value(CURR_STORE_LOCATION_CONF_NAME, store_location)

def get_applied_alt_store_name():
    alt_store_name = None
    config = read_config()
    commands_store_location = config.get(CURR_STORE_LOCATION_CONF_NAME)
    alt_stores = config.get(ALT_STORES_CONF_NAME)
    for store in alt_stores:
        if store.get(ALT_STORE_LOCATION_CONF_NAME) == commands_store_location:
            alt_store_name = store.get(ALT_STORE_NAME_CONF_NAME)
    return alt_store_name if alt_store_name else ''
