class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [3, 4, 5, 1, 2]
        While l <= r:
            Calculate mid
            If nums[mid] == target: return mid
            If mid < r (sorted):
                Check if target in [mid, r]:
                    yes -> binary search [mid+1, r]
                    no -> r = mid - 1
            If mid > r:
                Check if target in [l, mid]:
                    yes -> binary search [mid+1, r]
                    no -> l = mid + 1             
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
