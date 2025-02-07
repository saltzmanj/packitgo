from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_not_required

# Create your views here.

@login_not_required
def InventoryLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            if user.groups.filter(name='WarehouseManagers').exists():
                return redirect("/inventory/warehouse/")
            else:
                return redirect("/inventory/moveinventory/")
        else:
            context = {
                'is_failure': True
            }
            return render(request, "registration/login.html", context)
    else:
        return HttpResponse(status = 404)

def InventoryLogout(request):
    logout(request)
    return redirect("/accounts/login")

def Warehouse(request):
    context = {}
    return render(request, "inventory/warehouse.html", context)

def MoveInventory(request):
    context = {}
    return render(request, "inventory/scan1.html", context)


