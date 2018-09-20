from remoteControl import RemoteControl
import time

machineUrl = 'http://localhost:8000/1'

control = RemoteControl(machineUrl=machineUrl)
control.executeOrder()

# for i in range(10):
  # control.executeOrder()
  # time.sleep(1)
