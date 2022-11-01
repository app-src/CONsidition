import json

class Solution:
    def __init__(self, recycleRefundChoice, bagPrice, refundAmount, bagType):
        self.mapName = None
        self.recycleRefundChoice = recycleRefundChoice
        self.bagPrice = bagPrice
        self.refundAmount = refundAmount
        self.bagType = bagType
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)

    def addMapName(self, mapName):
        self.mapName = mapName

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
