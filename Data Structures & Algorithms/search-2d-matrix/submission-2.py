class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def binarySearch(l, h, submatrix, target):
            mid = l + ((h - l)//2)
            while l <= h:
                if submatrix[mid] == target:
                    return True
                elif submatrix[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1
                return binarySearch(l, h, submatrix, target)
            return False

        t, b = 0, m-1
        while t <= b:
            mid_row = t + ((b - t)//2)
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] > target:
                b = mid_row - 1
            else:
                if matrix[mid_row][n-1] < target:
                    t = mid_row + 1
                elif matrix[mid_row][n-1] > target:
                    #l, h = 1, n-2
                    return binarySearch(1, n-2, matrix[mid_row], target)
                else:
                    return True
        return False
