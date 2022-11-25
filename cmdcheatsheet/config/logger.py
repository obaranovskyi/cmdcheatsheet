from cmdcheatsheet.shared.logger import BLUE, GREEN


def config_details(config_key, config_value):
    if isinstance(config_value, list):
        print(f"[{BLUE}] {config_key}:")
        for config_dict in config_value:
            print(f"[{BLUE}]   {'-'*5}")
            for key in config_dict:
                config_details('  '+key, config_dict.get(key))
    else:
        print(f"[{BLUE}] {config_key}[{GREEN}]: {config_value}")
    
