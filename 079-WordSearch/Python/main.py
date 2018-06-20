class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        
        n, m = len(board), len(board[0])
        res = [False]
        size = len(word)
        letter = word[0]
        
        def dfs(i, j, depth, visited):
            if depth == size or res[0]:
                res[0] = True
                return
            if i < n - 1 and board[i+1][j] == word[depth] and (i+1, j) not in visited:
                visited |= set([(i+1,j)])
                dfs(i+1, j, depth+1, visited)
                visited.discard((i+1,j))
            if j < m - 1 and board[i][j+1] == word[depth] and (i, j+1) not in visited:
                visited |= set([(i,j+1)])
                dfs(i, j+1, depth+1, visited)
                visited.discard((i,j+1))
            if i > 0 and board[i-1][j] == word[depth] and (i-1, j) not in visited:
                visited |= set([(i-1,j)])
                dfs(i-1, j, depth+1, visited)
                visited.discard((i-1,j))
            if j > 0 and board[i][j-1] == word[depth] and (i, j-1) not in visited:
                visited |= set([(i,j-1)])
                dfs(i, j-1, depth+1, visited)
                visited.discard((i,j-1))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == letter:
                    dfs(i, j, 1, set([(i,j)]))
                    if res[0]:
                        return True
        
        return False