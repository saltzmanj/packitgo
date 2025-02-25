from inventory.models import Location, LocationType, InventoryTransactionStatus  # Adjust the import path based on your app structure
from django.core.management.base import BaseCommand

def create_test_locations():
    # Clear existing locations if needed
    # Location.objects.all().delete()  # Uncomment if you want to start fresh



    # List of test locations
    locations = [
        "Receiving Dock",
        "Main Warehouse",
        "Shipping Area",
        "Quality Control",
        "Assembly Line A",
        "Assembly Line B",
        "Raw Materials",
        "Finished Goods",
        "Returns Processing",
        "Overflow Storage"
    ]

    # Create locations
    for location_name in locations:
        Location.objects.get_or_create(locationName=location_name, locationType=LocationType.objects.get(description="DEFAULT"))
    
    print(f"Created {len(locations)} test locations")

    transactionStatuses = [
        "INPROGRESS",
        "COMPLETE"
    ]

    for transaction_status in transactionStatuses:
        InventoryTransactionStatus.objects.get_or_create(description = transaction_status)
    
    print(f"Created {len(transactionStatuses)} transaction statuses")

class Command(BaseCommand):
    help = 'Creates test locations in the database'

    def handle(self, *args, **kwargs):
        # Paste the create_test_locations function here
        create_test_locations()