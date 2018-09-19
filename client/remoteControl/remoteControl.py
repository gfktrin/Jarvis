import requests
import json


class RemoteControl:
  def __init__(
    self,
    ordersUrl,
  ):
    self.ordersUrl = ordersUrl
    self.order = None
    self.response_url = 'http://localhost:8000/test'

  def getOrderJson(self):
    orderRequest = requests.get(self.ordersUrl)
    self.order = orderRequest.text

  def getCleanOrder(self):
    orderJson = json.loads(self.order)
    return orderJson['order'].lower()

  def checkExecuted(self):
    orderJson = json.loads(self.order)
    return orderJson['executed']

  def sendResponse(self):
    response = requests.get(self.response_url)
    csrftoken = response.cookies['csrftoken']
    payload = {
              'executed':'True',
              }
    headers = {
              'Referer': self.response_url,
              'X-CSRFToken': csrftoken
              }
    cookie = {'csrftoken':csrftoken}
    requests.post(self.response_url, data=payload, headers=headers,cookies=cookie)
    self.order = None

  def executeOrder(self):
    self.getOrderJson()
    if(self.checkExecuted() == 'False'):
      if(self.getCleanOrder() == 'desligar'):
        self.sendResponse()
    else:
      return 'no orders to execute'
