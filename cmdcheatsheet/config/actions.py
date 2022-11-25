from cmdcheatsheet.config import *

config_actions = [
    display_available_configs.DisplayAvailableConfigs(),
    display_config.DisplayConfig(),
    remove_config.RemoveConfig(),
    set_config.SetConfig(),
    set_config_to_default.SetConfigToDefault(),
    set_single_config_to_default.SetSingleConfigToDefault()
]
