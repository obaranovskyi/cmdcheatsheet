from rich import print
from cmdcheatsheet.config.consts import ALT_STORE_LOCATION_CONF, ALT_STORE_NAME_CONF
from cmdcheatsheet.shared.display import BLUE, GREEN


def display_alt_store_list(alt_stores):
    for store in alt_stores:
        display_alt_store(store.get(ALT_STORE_NAME_CONF), store.get(ALT_STORE_LOCATION_CONF))

def display_alt_store(store_name, store_value):
    print(f"[{BLUE}]  {store_name}[{GREEN}] - {store_value}")

