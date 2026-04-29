class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        window = [0] * 26
        for ch in s1:
            idx = ord(ch) - ord("a")
            s1_count[idx] += 1
        for i in range(len(s2)):
            window[ord(s2[i]) - ord("a")] += 1
            if i >= len(s1):
                window[ord(s2[i-len(s1)]) - ord("a")] -= 1
            if window == s1_count:
                return True
        return False
