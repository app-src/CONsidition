import json

class Solution:
    def __init__(self, recycleRefundChoice, bagPrice, refundAmount, bagType):
        self.recycleRefundChoice = recycleRefundChoice
        self.bagPrice = bagPrice
        self.refundAmount = refundAmount
        self.bagType = bagType
        self.orders = []

    def addOrder(self, int):
        self.orders.append(int)

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))
