class Solution:
    def maxProfit(self,prices):
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                
            else:
                current_profit = prices[right] - prices[left]
                if max_profit < current_profit:
                    max_profit = current_profit
            right += 1
                    
        return max_profit
                