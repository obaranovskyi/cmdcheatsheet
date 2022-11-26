import json
from .display import display_error


def write_json(file_location, json_content):
    try:
        with open(file_location, 'w') as file_object:
            json.dump(json_content, file_object, indent=4)
    except Exception as _:
        display_error(f"Can't write to {file_location}")
