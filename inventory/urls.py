from django.urls import path
from . import views

app_name = "inventory"
urlpatterns = [
    path("InventoryLogin/", views.InventoryLogin, name="InventoryLogin"),

    path("warehouse/", views.Warehouse, name="Warehouse"),
    path("moveinventory/", views.MoveInventory, name="MoveInventory")
]