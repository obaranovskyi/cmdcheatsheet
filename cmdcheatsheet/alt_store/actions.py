# from cmdcheatsheet.alt_store import * 
from cmdcheatsheet.alt_store.add_alt_store import AddAltStore
from cmdcheatsheet.alt_store.delete_alt_store import DeleteAltStore
from cmdcheatsheet.alt_store.display_applied_alt_store_name import DisplayAppliedAltStoreName
from cmdcheatsheet.alt_store.display_available_alt_stores import DisplayAvailableAltStores
from cmdcheatsheet.alt_store.switch_to_alt_store import SwitchToAltStore
from cmdcheatsheet.alt_store.update_alt_store import UpdateAltStore

alt_store_actions = [
    AddAltStore(),
    DeleteAltStore(),
    DisplayAppliedAltStoreName(),
    DisplayAvailableAltStores(),
    SwitchToAltStore(),
    UpdateAltStore()
]
