class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mat = [[0 for _ in range(n)] for _ in range(n)]
        i, beg, end = 1, 0, n-1
        
        while beg < end:
            # horizonal upper
            for j in range(beg, end):
                mat[beg][j] = i
                i += 1
            
            # vertical right
            for j in range(beg, end):
                mat[j][end] = i
                i += 1
                
            # horizontal bottom
            for j in range(end, beg, -1):
                mat[end][j] = i
                i += 1            
            
            # vertical left
            for j in range(end, beg, -1):
                mat[j][beg] = i
                i += 1
            
            beg += 1
            end -= 1
        
        if beg == end:
            mat[beg][beg] = i
        
        return mat