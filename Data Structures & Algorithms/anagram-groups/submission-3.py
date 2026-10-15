class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list)
        for string in strs:
            count = [0]*26
            for ch in string:
                count[ord(ch)-ord('a')] += 1
            record[tuple(count)].append(string)
        return list(record.values())
