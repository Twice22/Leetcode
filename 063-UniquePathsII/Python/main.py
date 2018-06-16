class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        
        # initialize table
        table = [[0] * m for _ in range(n)]
        
        # initialize first row
        prev = 1
        for i in range(m):
            if prev:
                table[0][i] = 1 and (1-obstacleGrid[0][i])
                if not(table[0][i]):
                    prev = 0
            else:
                table[0][i] = 0
        
        # initialize first col
        prev = 1
        for j in range(n):
            if prev:
                table[j][0] = 1 and (1-obstacleGrid[j][0])
                if not(table[j][0]):
                    prev = 0
            else:
                table[j][0] = 0
        
        # comple table with DP
        for i in range(1, n):
            for j in range(1, m):
                if not(obstacleGrid[i][j]):
                    table[i][j] = table[i-1][j] + table[i][j-1]
        
        return table[-1][-1]
        