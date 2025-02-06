from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
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
            return HttpResponse(status = 200)
        else:
            context = {
                'is_failure': True
            }
            return render(request, "registration/login.html", context)
    else:
        return redirect("registration/login.html")

def Warehouse(request):
    return HttpResponse(status = 200)

def MoveInventory(request):
    return HttpResponse(status = 200)
