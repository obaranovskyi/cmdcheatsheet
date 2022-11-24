from cmdcheatsheet.config import read_config, set_config_value
from cmdcheatsheet.json_file import write_json
from cmdcheatsheet.consts import CONFIG_LOCATION
from cmdcheatsheet.display import display_alt_store


def add_alt_store(alt_store):
    config = read_config()
    alt_stores = config.get('alternativeStoreLocations')
    alt_stores.append({
        'storeName': alt_store.name,
        'storeLocation': alt_store.location 
    })
    write_json(CONFIG_LOCATION, config)
    
def update_alt_store(alt_store_to_update):
    config = read_config()
    for alt_store in config.get('alternativeStoreLocations') :
        if alt_store.get('storeName') == alt_store_to_update.name:
            alt_store['storeLocation'] = alt_store_to_update.location
    write_json(CONFIG_LOCATION, config)

def delete_alt_store(store_name):
    config = read_config()
    alt_stores = config.get('alternativeStoreLocations')
    config['alternativeStoreLocations'] = exclude_by_name_filter(alt_stores, store_name)
    write_json(CONFIG_LOCATION, config)

def is_existing_store_name(store_name):
    config = read_config()
    alt_stores = config.get('alternativeStoreLocations')
    alt_store_names = [store.get('storeName') for store in alt_stores]
    return store_name in alt_store_names

def exclude_by_name_filter(alt_stores, store_name):
    return [store for store in alt_stores if store.get('storeName') != store_name]

def display_alt_stores():
    display_alt_store(read_config().get('alternativeStoreLocations'))

def find_alt_store_by_name(store_name):
    config = read_config()
    return next((store for store in config.get('alternativeStoreLocations') if store.get('storeName') == store_name), None)

def switch_to_alt_store(store_name):
    alt_store = find_alt_store_by_name(store_name)
    store_location = alt_store.get('storeLocation')
    set_config_value('commandsStoreLocation', store_location)

def get_applied_alt_store_name():
    alt_store_name = None
    config = read_config()
    commands_store_location = config.get('commandsStoreLocation')
    alt_stores = config.get('alternativeStoreLocations')
    for store in alt_stores:
        if store.get('storeLocation') == commands_store_location:
            alt_store_name = store.get('storeName')
    return alt_store_name if alt_store_name else ''
