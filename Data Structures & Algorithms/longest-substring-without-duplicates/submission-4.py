class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     track = set()
    #     l = 0
    #     res = 0

    #     for r in range(len(s)):
    #         while s[r] in track:
    #             track.remove(s[l])
    #             l+=1
    #         track.add(s[r])
    #         res = max(res, r-l+1)

    #     return res

        # what about jump to the last seen position
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = {} # char -> index
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] in track and track[s[r]] >= l:
                l = track[s[r]] + 1
                
            track[s[r]] = r
            res = max(res, r-l+1)
        
        return res
