class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next_day_prices = list(prices)
        profits = []
        for i in prices:
            
            current_price = i
            difference = 0
            next_day_prices.remove(current_price)
            
            for j in next_day_prices:
                diff = j -i
                if(difference < diff):
                    difference = diff
            
            profits.append(difference)
      
        return max(profits)
            
                
            