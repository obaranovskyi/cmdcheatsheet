from cmdcheatsheet.config.consts import ALT_STORE_LOCATION_CONF, ALT_STORE_NAME_CONF
from cmdcheatsheet.shared.logger import BLUE, GREEN


def display_alt_store(alt_stores):
    for store in alt_stores:
        alt_store_details(store.get(ALT_STORE_NAME_CONF), store.get(ALT_STORE_LOCATION_CONF))

def alt_store_details(store_name, store_value):
    print(f"[{BLUE}]  {store_name}[{GREEN}] - {store_value}")

