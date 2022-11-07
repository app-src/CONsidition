import operator

from solution import Solution


class Solver:
    bagType_price = [1.7, 1.75, 6, 25, 200]
    bagType_co2_transport = [3.0, 4.2, 1.8, 3.6, 12.0]
    bagType_co2_production = [30, 24, 36, 42, 60]

    def __init__(self, game_info):
        try:
            self.days = None
            self.population = game_info["population"]
            self.companyBudget = game_info["companyBudget"]
            self.behavior = game_info["behavior"]
        except:
            print("Error in Solver.__init__")


    def Solve(self, bagtype, days,choices=0,recycleRefundChoice=0,refundAmountMultiplicationFactor=1):
        self.days = days
        solution = Solution(recycleRefundChoice, self.bagType_price[bagtype-1],self.bagType_price[bagtype-1]*1, bagtype)
        
        for day in choices:
            solution.addOrder(day)

        
        return solution

    
    # Solution 1: "Spend all money day 1"
    def wasteMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype])

    # Solution 2: "Spend equally money every day"
    def splitMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype] / self.days)

    # Solution 3: "Everyone get one bag every day"
    def holdMoney(self, bagtype):
        return int(self.companyBudget / self.bagType_price[bagtype] / self.population / self.days)
