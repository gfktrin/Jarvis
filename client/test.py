from remoteControl import RemoteControl
import time

machineUrl = 'http://localhost:8000/1'

control = RemoteControl(machineUrl=machineUrl)
loop_control = False

while loop_control == False:
   control.executeOrder()
   time.sleep(1)
