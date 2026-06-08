class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [4, 5, 6, 7, 0, 1, 2, 3]
        while l < r:
            calculate mid idx
            if nums[mid] > nums[r]:
                search right [mid+1, r]
            else:
                search left [l, mid]
        return nums[l]
        '''

        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]