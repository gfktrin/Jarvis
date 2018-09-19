import requests
import json


class RemoteControl:
  def __init__(
    self,
    ordersUrl,
  ):
    self.ordersUrl = ordersUrl
    self.order = None

  def getOrderJson(self):
    orderRequest = requests.get(self.ordersUrl)
    self.order = orderRequest.text

  def getCleanOrder(self):
    orderJson = json.loads(self.order)
    return orderJson['order']

  def checkExecuted(self):
    orderJson = json.loads(self.order)
    return orderJson['executed']

  def executeOrder(self):
    self.getOrderJson()
    if(self.checkExecuted() == 'False'):
      return 'OK'
    else:
      return 'no orders to execute'
