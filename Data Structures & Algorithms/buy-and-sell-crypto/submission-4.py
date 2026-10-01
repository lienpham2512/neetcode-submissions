class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for p in prices:
            min_price = min(p, min_price)
            profit = max(profit, p - min_price)

        return profit