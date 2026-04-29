class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums)-1
            while j < k:
                threeSum = val + nums[j] + nums[k]
                if threeSum == 0:
                    res.append([val, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif threeSum > 0:
                    k-=1
                else:
                    j+=1
        return res