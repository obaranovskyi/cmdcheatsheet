from .add_alt_store import AddAltStore
from .delete_alt_store import DeleteAltStore
from .display_applied_alt_store_name import DisplayAppliedAltStoreName
from .display_available_alt_stores import DisplayAvailableAltStores
from .switch_to_alt_store import SwitchToAltStore
from .update_alt_store import UpdateAltStore

alt_store_actions = [
    AddAltStore(),
    DeleteAltStore(),
    DisplayAppliedAltStoreName(),
    DisplayAvailableAltStores(),
    SwitchToAltStore(),
    UpdateAltStore()
]
