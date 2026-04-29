class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_freq = [0] * 26
        max_count = 0
        res = 0
        l = 0

        for r in range(len(s)):
            char_index = ord(s[r]) - ord('A')
            count_freq[char_index] += 1
            max_count = max(max_count, count_freq[char_index])

            # shrink if we don't have enough k to replace
            while r - l + 1 - max_count > k:
                i = ord(s[l]) - ord('A')
                count_freq[i] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
