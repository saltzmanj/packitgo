from inventory.models import Part, Batch, Location, InventoryTransaction


'''
1. if inventory_available < moved_location
    return error

2. newTxn = InventoryTransaction(
status = in_progress

)


'''
def startInventoryMove(part, batch, qty, fromLocation, toLocation):


