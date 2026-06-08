class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary search [1, max(piles)]
        validate: deduct ceil(pile/k) from h, invalid if h < 0
        if valid, search lower bound, if not, search upper bound until valid
        '''

        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l)//2
            hour = h
            for p in piles:
                hour -= math.ceil(p/mid)
            if hour < 0:
                l = mid + 1
            else:
                r = mid
        return l