from .display import display_error

def show_invalid_store_location_message():
    display_error("Something is wrong with your JSON file. The issue might appear due to the following:\n" +
          "1. The file location is wrong.\n" +
          "2. The file content is not a list of commands.")
