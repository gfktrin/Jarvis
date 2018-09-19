from remoteControl import RemoteControl
import time

ordersUrl = 'http://localhost:8000/1/order'

control = RemoteControl(ordersUrl=ordersUrl)
# print(control.executeOrder())

for i in range(10):
  control.executeOrder()
  time.sleep(1)
