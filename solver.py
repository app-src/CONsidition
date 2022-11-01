import operator

from solution import Solution


class Solver:
    bagType_price = [1.7, 1.75, 6, 25, 200]
    bagType_co2_production = [5, 7, 3, 6, 20]
    bagType_co2_transport = [50, 40, 60, 70, 100]

    def __init__(self, game_info):
        self.days = None
        self.population = game_info["population"]
        self.companyBudget = game_info["companyBudget"]
        self.behavior = game_info["behavior"]

    def Solve(self, bagtype, days):
        self.days = days
        solution = Solution(True, 10, 1, bagtype)

        for day in range(0, days):
            solution.addOrder(self.wasteMoney(bagtype))
        
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
