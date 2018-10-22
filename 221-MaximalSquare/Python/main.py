class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        h = len(matrix)
        w = len(matrix[0])

        max_area = 0
        dp = [[0] * w for i in range(h)]
        for x in range(w):
            dp[0][x] = int(matrix[0][x])
            max_area = max(max_area, dp[0][x])
        for y in range(h):
            dp[y][0] = int(matrix[y][0])
            max_area = max(max_area, dp[y][0])

        for y in range(1, h):
            for x in range(1, w):
                if matrix[y][x] == "0":
                    dp[y][x] = 0
                else:
                    dp[y][x] = min([dp[y-1][x], dp[y][x-1], dp[y-1][x-1]]) + 1
                max_area = max(max_area, dp[y][x])

        return max_area ** 2