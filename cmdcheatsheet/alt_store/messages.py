from cmdcheatsheet.shared.logger import error

def show_store_with_name_not_exists(store_name):
    error(f"A store with the name {store_name} does not exist.")

