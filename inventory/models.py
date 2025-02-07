# from django.db import models

# # Create your models here.
# class InventoryRecord(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
#     quantity = models.FloatField()


# class Location(models.Model):
#     locationName = models.CharField(max_length=100)
#     locationType = models.ForeignKey(LocationType, on_delete=models.CASCADE)

# class LocationType(models.Model):
#     description = models.TextField()

# class Batch(models.Model):
#     part = models.ForeignKey(Part, on_delete=models.CASCADE)
#     batchNumber = models.FloatField()
#     quantity = models.FloatField()

# class Part(models.Model):
#     partNumber = models.FloatField()
#     name = models.CharField(max_length=100)

# class InventoryTransaction(models.Model):
#     fromLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
#     toLocation = models.ForeignKey(Location, on_delete=models.CASCADE)
#     quantity = models.FloatField()
#     batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     duration = models.FloatField()
#     statusId = models.ForeignKey(InventoryTransactionStatus, on_delete=models.CASCADE)
#     timeStamp = models.DateField()

# class InventoryTransactionStatus(models.Model):
#     description = models.TextField()