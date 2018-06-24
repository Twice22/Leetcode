class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        # constant space solution for the win
        # idea: go through all elements in the matrix
        # for each 0 in the matrix put a 0 in the first row, first col:
        # so, if row[i][j] = 0 --> row[0][j] = 0 and row[i][0] = 0
        # then go through first row/first col and put 0 the the rest of the
        # col/row
        if not matrix or (matrix and not matrix[0]):
            return matrix
        
        n, m = len(matrix), len(matrix[0])
        ver, hor = 0, 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if j == 0:
                        ver = 1 # 0 comes from row
                    if i == 0:
                        hor = 1 # 0 comes from hor

        # go through first row and set cols to 0
        for j in range(1,m):
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0

        # go through first col and set rows to 0
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(m):
                    matrix[i][j] = 0
        
        # edge case
        if matrix[0][0] == 0:
            if ver:
                for i in range(n):
                    matrix[i][0] = 0
            if hor:
                for j in range(m):
                    matrix[0][j] = 0
        