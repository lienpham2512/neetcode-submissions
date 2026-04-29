class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums_set:
            prev = num - 1
            if prev not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                longest_length = max(longest_length, length)
        return longest_length
