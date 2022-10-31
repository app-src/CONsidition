import operator

class Solver:
    bagType_price = [1.7, 1.75, 6, 25, 200]
    bagType_co2_production = [5, 7, 3, 6, 20]
    bagType_co2_transport = [50, 40, 60, 70, 100]

    def __init__(self, game_info):
        self.population = game_info["population"]
        self.companyBudget = game_info["companyBudget"]
        self.behavior = game_info["behavior"]

    def Solve(self, bagtype, days):
        solution.recycleRefundChoice = "True"
        solution.bagPrice = 10
        solution.refundAmount = 1
        solution.bagType = 1
        
        solution.orders = []
        for day in range(0, days):
            solution.orders.append(wasteMoney(bag_type))
        
        return solution


    # Solution 1: "Spend all money day 1"
    def wasteMoney(bagtype):
        return int(companyBudget / bagType_price[bagtype])

    # Solution 2: "Spend equally money every day"
    def splitMoney(bagtype):
        return int(companyBudget / bagType_price[bagtype] / days)

    # Solution 3: "Everyone get one bag every day"
    def holdMoney(bagtype):
        return int(companyBudget / bagType_price[bagtype] / population / days)