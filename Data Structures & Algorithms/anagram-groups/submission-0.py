class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # key: tuple (cannot be list), value: list of strings
        for word in strs:
            count = [0] * 26 # 26 characters
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            res[key].append(word)
        return list(res.values())
