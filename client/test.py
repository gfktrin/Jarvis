from remoteControl import RemoteControl

ordersUrl = 'http://localhost:8000/1/order'

control = RemoteControl(ordersUrl=ordersUrl)
print(control.executeOrder())
print(control.getCleanOrder())
