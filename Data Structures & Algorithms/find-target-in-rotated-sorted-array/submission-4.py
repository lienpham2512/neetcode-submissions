class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        break_point = l

        # we got the break point mid
        l, r = 0, len(nums)-1
        if target <= nums[r]:
            l = break_point
        else:
            r = break_point - 1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1            
        return -1