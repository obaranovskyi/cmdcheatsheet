from cmdcheatsheet.logger import error
from cmdcheatsheet.config import read_config
from cmdcheatsheet.json_file import write_json
from cmdcheatsheet.consts import config_location
from cmdcheatsheet.display import display_alternative_store

def add_alternative_store(store_name, store_location):
    config = read_config()
    alternative_stores = config.get('alternativeStoreLocations')
    alternative_stores.append({
        'storeName': store_name,
        'storeLocation': store_location
    })
    write_json(config_location, config)
    
def update_alternative_store(store_name, store_location):
    config = read_config()
    for store in config.get('alternativeStoreLocations') :
        if store.get('storeName') == store_name:
            store['storeLocation'] = store_location
    write_json(config_location, config)

def delete_alternative_store(store_name):
    config = read_config()
    alternative_stores = config.get('alternativeStoreLocations')
    config['alternativeStoreLocations'] = exclude_by_name_filter(alternative_stores, store_name)
    write_json(config_location, config)

def is_existing_store_name(store_name):
    config = read_config()
    alternative_stores = config.get('alternativeStoreLocations')
    alternative_store_names = [store.get('storeName') for store in alternative_stores]
    return store_name in alternative_store_names

def exclude_by_name_filter(alternative_stores, store_name):
    return [store for store in alternative_stores if store.get('storeName') != store_name]

def display_alternative_stores():
    display_alternative_store(read_config().get('alternativeStoreLocations'))

