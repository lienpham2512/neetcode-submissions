class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        def calculateArea(a, b, heights):
            return min(heights[a], heights[b])*abs(a-b)
        
        l, r = 0, len(heights)-1
        while l < r:
            newArea = calculateArea(l, r, heights)
            area = max(area, newArea)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return area