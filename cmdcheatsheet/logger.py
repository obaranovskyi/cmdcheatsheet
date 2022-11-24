from rich import print


blue = "turquoise2"
red = "deep_pink2"
green = "spring_green1"
yellow = "yellow"

def info(message):
    print(f"[{blue}]{message}")

def error(message):
    print(f"[{red}]{message}")

def command_details(command, display_index, id_column_length=5):
    id = str(command.id) + ' '*(id_column_length - len(str(command.id)))
    index = f"[{blue}]|[{yellow}] {id}[{blue}]  |" if display_index else ""
    print(f"{index}[{blue}] {command.command}[{green}] - {command.description}")

def help_details(command_name, description):
    print(f"[{blue}]  {command_name}[{green}] - {description}")

def alternative_store_details(store_name, store_value):
    print(f"[{blue}]  {store_name}[{green}] - {store_value}")

def config_details(config_key, config_value):
    if isinstance(config_value, list):
        print(f"[{blue}] {config_key}:")
        for config_dict in config_value:
            print(f"[{blue}]   {'-'*5}")
            for key in config_dict:
                config_details('  '+key, config_dict.get(key))
    else:
        print(f"[{blue}] {config_key}[{green}]: {config_value}")
    
def version_details(current_version):
    print(f"[{blue}] Version: [{green}]{current_version}")
