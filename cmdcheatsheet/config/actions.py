from cmdcheatsheet.config.display_available_configs import DisplayAvailableConfigs
from cmdcheatsheet.config.display_config import DisplayConfig
from cmdcheatsheet.config.remove_config import RemoveConfig
from cmdcheatsheet.config.set_config import SetConfig
from cmdcheatsheet.config.set_config_to_default import SetConfigToDefault
from cmdcheatsheet.config.set_single_config_to_default import SetSingleConfigToDefault

config_actions = [
    DisplayAvailableConfigs(),
    DisplayConfig(),
    RemoveConfig(),
    SetConfig(),
    SetConfigToDefault(),
    SetSingleConfigToDefault()
]
