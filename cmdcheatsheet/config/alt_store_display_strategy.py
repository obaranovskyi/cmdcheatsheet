from rich import print
from rich.tree import Tree
from .consts import ALT_STORE_LOCATION_CONF, ALT_STORE_NAME_CONF, ALT_STORES_CONF
from .core import read_config
from .models import DisplayStrategy
from cmdcheatsheet.shared.display import BLUE, GREEN


class AltStoreDisplayStrategy(DisplayStrategy):

    def __init__(self):
        config = read_config()
        alt_stores = config.get(ALT_STORES_CONF)
        super().__init__(ALT_STORES_CONF, alt_stores)

    def display(self):
        if not self.config_value:
            print(f"[{BLUE}]{self.config_key}: [{GREEN}] <empty>")
            return
        tree = Tree(f"[{BLUE}]{self.config_key}:")
        for config_dict in self.config_value:
            tree.add(
                f"[{BLUE}]{config_dict[ALT_STORE_NAME_CONF]}:" +
                f"[{GREEN}]{config_dict[ALT_STORE_LOCATION_CONF]}"
            )
        print(tree)

