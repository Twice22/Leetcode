class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        beg, end = 0, len(matrix[0])
        
        while beg < end:
            for i in range(beg+1, end):
                matrix[beg][i], matrix[i][end-1], matrix[end-1][-i-1], matrix[-i-1][beg] = matrix[-i-1][beg], matrix[beg][i], matrix[i][end-1], matrix[end-1][-1-i]

            beg += 1
            end -= 1