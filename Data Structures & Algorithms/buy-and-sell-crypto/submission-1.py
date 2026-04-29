class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice, profit = prices[0], 0
        for price in prices:
            if price > buyPrice:
                profit = max(profit, (price - buyPrice))
            else:
                buyPrice = price
        return profit