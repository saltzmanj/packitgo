from django.db import models

# Create your models here.
class LocationType(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description 

class Location(models.Model):
    locationName = models.CharField(max_length=100)
    locationType = models.ForeignKey(LocationType, on_delete=models.CASCADE)

    def __str__(self):
        return self.locationName 

class Part(models.Model):
    partNumber = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class Batch(models.Model):
    partNumber = models.ForeignKey(Part, on_delete=models.CASCADE)
    batchNumber = models.CharField(max_length=100)


class InventoryRecord(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    quantity = models.FloatField()

class InventoryTransactionStatus(models.Model):
    description = models.CharField(max_length=100)

class InventoryTransaction(models.Model):
    fromLocation = models.ForeignKey(Location, related_name="fromLocation", on_delete=models.CASCADE)
    toLocation = models.ForeignKey(Location, related_name="toLocation", on_delete=models.CASCADE)
    quantity = models.FloatField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.FloatField(null=True)
    statusId = models.ForeignKey(InventoryTransactionStatus, on_delete=models.CASCADE)
    timeStamp = models.DateField()

