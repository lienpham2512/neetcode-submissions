class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]

        while l < r:
            if maxR < maxL:
                r -= 1
                maxR = max(maxR, height[r])
                water += (maxR - height[r])
            else:
                l += 1
                maxL = max(maxL, height[l])
                water += (maxL - height[l])
        return water
        