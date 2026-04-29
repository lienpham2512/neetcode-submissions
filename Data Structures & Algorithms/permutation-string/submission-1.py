class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        two lists to count, if == then true, else false
        add s1 to list 1
        then sliding window on s2 to find the same list as s1
        '''
        if len(s1) > len(s2):
            return False

        l1, l2 = [0]*26, [0]*26

        for ch in s1:
            index = ord(ch)-ord('a')
            l1[index] += 1
        
        windowSize = len(s1)

        for i in range(len(s2)):
            l2[ord(s2[i]) - ord('a')] += 1

            if i >= windowSize:
                l2[ord(s2[i - windowSize]) - ord('a')] -= 1

            if l1 == l2:
                return True
            
        return False

