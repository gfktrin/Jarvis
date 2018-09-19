import requests
import json


class RemoteControl:
  def __init__(
    self,
    ordersUrl,
  ):
    self.ordersUrl = ordersUrl

  def getOrderJson(self):
    orderRequest = requests.get(self.ordersUrl)
    return orderRequest.text

  def getCleanOrder(self):
    orderJson = json.loads(self.getOrderJson())
    return orderJson['order']

