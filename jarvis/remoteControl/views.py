from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Order,Machine

# Create your views here.
def order_return(request,machine):
    order = Order.objects.filter(machineId=machine).latest('createdAt')
    jsonResponse = {
        'orderId' : str(order.id),
        'command' : order.command,
        'machine' : str(order.machineId),
        'createdAt' : str(order.createdAt),
        'executed' : str(order.executed),
        'silentMode' : str(order.silentMode),
    }
    return JsonResponse(jsonResponse)

def submit_machine_response(request,machine):
    machine = Machine.objects.filter(id=machine)

    if request.method == 'POST':
        machine.update(lastConnected=timezone.now())
        machine_response = dict(request.POST)
        order = Order.objects.filter(id=machine_response['orderId'][0])
        command = order.values('command')[0]['command']
        print(machine_response)
        if(machine_response['executed'][0]=='True'):
            order.update(executed=True)
        if command == 'informações':
            print('ok')
            machine.update(os=machine_response['os'][0])
            machine.update(ip=machine_response['ip'][0])
            machine.update(mac=machine_response['mac'][0])
            machine.update(location=machine_response['location'][0])


        return HttpResponse('')
    if request.method == 'GET':
        return render(request, 'remoteControl/token.html', {})

def user_make_orders(request, user):
    return render(request, 'remoteControl/makeorder.html', {})
