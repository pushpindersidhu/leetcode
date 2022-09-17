class Solution:
    def __init__(self):
        self.hasStock = False
        self.boughtPrice = None
        self.profit = 0
    
    def maxProfit(self, prices: list[int]) -> int:
        days = len(prices)

        if days == 0 or days == 1:
            return 0
        
        for day in range(len(prices)):
            currentDayPrice = prices[day]
            if day == len(prices) - 1:
                if self.hasStock:
                    self.profit += currentDayPrice - self.boughtPrice
                return self.profit

            nextDayPrice = prices[day + 1]

            if nextDayPrice > currentDayPrice:
                if not self.hasStock:
                    self.hasStock = True
                    self.boughtPrice = currentDayPrice

            else:
                if self.hasStock:
                    if currentDayPrice > self.boughtPrice:
                        self.profit += currentDayPrice - self.boughtPrice
                        self.hasStock = False

        return self.profit


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    solution = Solution()
    print(solution.maxProfit(prices))
