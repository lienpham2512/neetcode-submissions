class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            rate_k = l + ((r-l)//2) # rate_k is the mid value
            hour_finish = 0
            for pile in piles:
                hour_finish += math.ceil(pile/rate_k)
            if hour_finish <= h:
                if rate_k < res:
                    res = rate_k
                r = rate_k - 1
            else:
                l = rate_k + 1
        return res
