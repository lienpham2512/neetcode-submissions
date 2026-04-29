class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in track:
                return [track[difference], index]
            else:
                track[value] = index
        

