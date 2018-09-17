from django.shortcuts import render
from django.utils import timezone
from .models import Order

# Create your views here.
def order_list(request,machine):
    order = Order.objects.filter(machineId=machine).latest('createdAt')
    return render(request, 'remoteControl/order_list.html', {'order': order})
