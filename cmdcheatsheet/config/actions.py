from .display_available_configs import DisplayAvailableConfigs
from .display_config import DisplayConfig
from .remove_config import RemoveConfig
from .set_config import SetConfig
from .set_config_to_default import SetConfigToDefault
from .set_single_config_to_default import SetSingleConfigToDefault

config_actions = [
    DisplayAvailableConfigs(),
    DisplayConfig(),
    RemoveConfig(),
    SetConfig(),
    SetConfigToDefault(),
    SetSingleConfigToDefault()
]
