from inventory.models import Part, Batch, Location, InventoryTransaction, InventoryRecord


'''
1. if inventory_available < moved_location
    return error

2. newTxn = InventoryTransaction(
status = in_progress

)


'''
def startInventoryMove(part, batch, qty, fromLocation, toLocation):
    # Get or create part
    part_obj, part_created = Part.objects.get_or_create(
        part_number=part
    )

    # Get or create batch
    batch_obj, batch_created = Batch.objects.get_or_create(
        batch_number=batch,
        part=part_obj
    )

    # Check available inventory in source location
    try:
        inventory_record = InventoryRecord.objects.get(
            part=part_obj,
            batch=batch_obj,
            location=fromLocation
        )
        if inventory_record.quantity < qty:
            raise ValueError(f"Insufficient inventory. Requested: {qty}, Available: {inventory_record.quantity}")
    except InventoryRecord.DoesNotExist:
        raise ValueError(f"No inventory found for part {part} batch {batch} in location {fromLocation}")

    # ... existing code ...
