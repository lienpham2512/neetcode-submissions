class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            hour = 0
            mid = l + (r-l)//2
            for p in piles:
                hour += math.ceil(p/mid)
            if hour > h:
                l = mid + 1
            else:
                r = mid
        return l