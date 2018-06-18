class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (not matrix) or (matrix and not matrix[0]):
            return False
        
        # it smells binary search!
        rows, cols = len(matrix), len(matrix[0])
        beg, end = 0, rows * cols - 1
        
        while beg <= end:
            mid = (beg + end) // 2
            x = mid // cols
            y = (mid - x * cols)

            if matrix[x][y] == target:
                return True
            
            if matrix[x][y] > target:
                end = mid-1
            else:
                beg = mid+1
        
        return False