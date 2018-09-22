class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        height = len(board)
        width = len(board[0])
        
        # add all "O" on the borders to a set
        circles = []
        def analyze(x, y):
            if board[x][y] == "O":
                circles.append((x,y))
        
        for h in range(height):
            analyze(h, width-1)
            analyze(h, 0)
            
        for w in range(width):
            analyze(0, w)
            analyze(height-1, w)
        
        # once all "O" from the border are added
        # we just need to do a BFS/DFS to add all
        # "O" that are connected horizontally or
        # vertically to the O from the border. We add
        # then to a set of "connected components"
        # finally we iterate through the whole board
        # and each time we encounter an "O" that is not
        # in the set of the "connected components" we switch
        # it to "X"
        connected = set()
        
        while circles:
            # simulate pop first element (BFS)
            x, y = circles[0]
            del circles[0]
            
            if (x,y) in connected:
                continue
            
            if x+1 < height: analyze(x+1, y)          
            if x-1 >= 0: analyze(x-1, y)
            if y+1 < width: analyze(x, y+1)
            if y-1 >= 0: analyze(x, y-1)
                
            connected.add((x, y))
        
        for h in range(1,height-1):
            for w in range(1,width-1):
                if (h, w) not in connected and board[h][w] == "O":
                    board[h][w] = "X"
                