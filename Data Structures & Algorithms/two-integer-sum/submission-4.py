class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for index, value in enumerate(nums):
            diff = target - value
            if diff in track:
                return [track[diff], index]
            track[value] = index