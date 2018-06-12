class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        n, m = len(matrix), len(matrix[0])
        result = []
        
        beg, end = 0, m-1
        beg1, end1 = 0, n-1
        while beg < end or beg1 < end1:
            for i in range(beg, end):
                result.append(matrix[beg1][i])
            
            if len(result) >= n*m:
                return result[:n*m]
            
            for i in range(beg1, end1):
                result.append(matrix[i][end])
            
            for i in range(end, beg, -1):
                result.append(matrix[end1][i])
            
            if len(result) >= n*m:
                return result[:n*m]
            
            for i in range(end1, beg1, -1):
                result.append(matrix[i][beg])
            
            beg += 1
            end -= 1
            beg1 += 1
            end1 -= 1
            
        if beg == beg1 == end == end1:
            result.append(matrix[beg][beg])
        
        return result[:n*m]