class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        track freq by dict
        constraint length - K = max in freq
        iterate through string s, count freq, check constraint -> record length
        if constraint is not met, move l ptr and recount the freq until constraint true
        '''

        l = 0
        freq = [0] * 26
        res = 0
        max_freq = 0

        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            freq[index] += 1
            max_freq = max(max_freq, freq[index])
            while r-l+1 - max_freq > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r-l+1)

        return res