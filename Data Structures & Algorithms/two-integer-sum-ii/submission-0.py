class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        diff = target - numbers[left]
        while left < right:
            if numbers[right] > diff:
                right -= 1
            elif numbers[right] < diff:
                left += 1
                diff = target - numbers[left]
            else:
                return [left+1, right+1]
        return []