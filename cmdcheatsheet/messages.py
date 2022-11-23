from cmdcheatsheet.logger import error

def show_store_with_name_not_exists(store_name):
    error(f"A store with the name {store_name} does not exist.")

def show_invalid_store_location_message():
    error("Something is wrong with your JSON file. The issue might appear due to the following:\n" +
          "1. The file location is wrong.\n" +
          "2. The file content is not a list of commands.")
