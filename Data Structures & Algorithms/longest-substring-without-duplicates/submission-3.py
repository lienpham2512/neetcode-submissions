class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        longest -> use max(current, new)
        no dup -> use set
        iterate r, if meet duplicated (check by set) we shrink by l
        sliding window
        '''

        l = 0
        res = 0
        record = set()
        for r in range(len(s)):
            while s[r] in record:
                record.remove(s[l])
                l += 1

            record.add(s[r])
            res = max(res, r-l+1)

        return res
            