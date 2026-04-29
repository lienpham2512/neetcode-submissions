class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength