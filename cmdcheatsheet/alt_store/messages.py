from cmdcheatsheet.shared.display import display_error

def show_store_with_name_not_exists(store_name):
    display_error(f"A store with the name {store_name} does not exist.")

