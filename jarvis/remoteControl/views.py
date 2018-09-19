from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Order

# Create your views here.
def order_return(request,machine):
    order = Order.objects.filter(machineId=machine).latest('createdAt')
    jsonResponse = {
        'orderId' : str(order.id),
        'order' : order.command,
        'machine' : str(order.machineId),
        'createdAt' : str(order.createdAt),
        'executed' : str(order.executed),
        'silentMode' : str(order.silentMode),
    }
    return JsonResponse(jsonResponse)

def submit_machine_response(request):
    if request.method == 'POST':
        print('Post: "%s"' % request.POST)
        print('Body: "%s"' % request.body)
        return HttpResponse('')
    if request.method == 'GET':
        return render(request, 'remoteControl/token.html', {})
