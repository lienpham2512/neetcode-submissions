class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for i in nums:
            if i in dic:
                return True
            dic.add(i)
        return False