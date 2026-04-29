from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = defaultdict(list)
        for s in strs:
            anagram = [0] * 26
            for ch in s:
                anagram[ord(ch)-ord('a')] += 1
            track[tuple(anagram)].append(s)
        return list(track.values())