class Solution:
    def livingNeighbors(self, arr, i, j, h, w):
        neighbors = 0
        
        if i+1 < h:
            neighbors += arr[i+1][j] & 1
            
            if j+1 < w:
                neighbors += arr[i+1][j+1] & 1
            if j-1 >= 0:
                neighbors += arr[i+1][j-1] & 1
    
        if j+1 < w:
            neighbors += arr[i][j+1] & 1
        if j-1 >= 0:
            neighbors += arr[i][j-1] & 1
        
        if i-1 >= 0:
            neighbors += arr[i-1][j] & 1
            
            if j+1 < w:
                neighbors += arr[i-1][j+1] & 1
            if j-1 >= 0:
                neighbors += arr[i-1][j-1] & 1
        
        return neighbors
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        
        h = len(board)
        w = len(board[0])
        
        ret = [[0] * w for _ in range(h)]
        
        for i in range(h):
            for j in range(w):
                if board[i][j] == 1:
                    if self.livingNeighbors(board, i, j, h, w) in {2,3}:
                        board[i][j] = 11
                    elif self.livingNeighbors(board, i, j, h, w) < 2:
                        board[i][j] = 13
                    else:
                        board[i][j] = 13
                elif board[i][j] == 0 and self.livingNeighbors(board, i, j, h, w) == 3:
                    board[i][j] = 14
                    
        for i in range(h):
            for j in range(w):
                if board[i][j] == 11:
                    board[i][j] = 1
                elif board[i][j] == 13:
                    board[i][j] = 0
                elif board[i][j] == 14:
                    board[i][j] = 1
                