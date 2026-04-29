class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # approach: track the matches count, more optimal bc we do not compare the lists 

        s1Count, s2Count = [0]*26, [0]*26
        for c in range(len(s1)):
            s1Count[ord(s1[c]) - ord('a')] += 1
            s2Count[ord(s2[c]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            if s1Count[idx] == s2Count[idx]:
                matches -= 1
            s2Count[idx] += 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1

            idx = ord(s2[l]) - ord('a')
            if s1Count[idx] == s2Count[idx]:
                matches -= 1
            s2Count[idx] -= 1
            if s1Count[idx] == s2Count[idx]:
                matches += 1

            l += 1


        return matches == 26