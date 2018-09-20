import requests
import json
import time
import platform
from uuid import getnode as get_mac
import socket
import geocoder

class RemoteControl:
  def __init__(
    self,
    machineUrl,
  ):
    self.machineUrl = machineUrl
    self.order = None
    self.os = platform.system()

  def getOrderJson(self):
    orderUrl = self.machineUrl+'/order'
    orderRequest = requests.get(orderUrl)
    self.order = orderRequest.text

  def getCleanOrder(self):
    orderJson = json.loads(self.order)
    return orderJson['command'].lower()

  def checkExecuted(self):
    orderJson = json.loads(self.order)
    return orderJson['executed']

  def sendResponse(self, payload):
    responseUrl = self.machineUrl+'/response'
    time.sleep(1)
    response = requests.get(responseUrl)
    csrftoken = response.cookies['csrftoken']
    # payload = {
    #           'executed':'True',
    #           }
    headers = {
              'Referer': responseUrl,
              'X-CSRFToken': csrftoken
              }
    cookie = {'csrftoken':csrftoken}
    requests.post(responseUrl, data=payload, headers=headers,cookies=cookie)
    self.order = None

  def getMachineInfoPayload(self):
    mac = get_mac()
    mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
    ip = socket.gethostbyname(socket.gethostname())
    location = geocoder.ip('me').address
    payload = {
      'executed':'True',
      'os':self.os,
      'mac':mac,
      'ip':ip,
      'location':location,
    }
    return payload

  def executeOrder(self):
    self.getOrderJson()
    if(self.checkExecuted() == 'False'):
      if(self.getCleanOrder() == 'desligar'):
        self.sendResponse()
      elif(self.getCleanOrder() == 'informações'):
        self.sendResponse(payload=self.getMachineInfoPayload())
    else:
      return 'no orders to execute'
