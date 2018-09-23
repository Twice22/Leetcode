import copy

# inefficient but working solution
# inefficient due to the memory overhead (clean and update grid)
class Solution:
    def totalNQueens2(self, n):
        """
        :type n: int
        :rtype: int
        """
        grid = [[0] * n for _ in range(n)]
        
        # put 1 in the:
        # - bottom left -> top right direction
        # - top left -> bottom right direction
        # - horizontal direction
        # don't need other directions as we will
        # put a queen in each column and advance
        # from column to column...
        def update(grid, x, y):
            for i in range(x, n):
                if y-x+i < n:
                    grid[i][y-x+i] = 1
            for i in range(y, n):
                grid[x][i] = 1
                if x+y-i >= 0:
                    grid[x+y-i][i] = 1            
        
        self.c = 0
        
        def helper(grid, col):
            
            # if we put all the queen on the board
            # and none of them jeopardize each others
            # increment the number of possibilities
            if col == n:
                self.c += 1
                return
            
            for i in range(n):
                # if we are allowed to put a queen, do it
                if grid[i][col] != 1:
                    cleaned_grid = copy.deepcopy(grid)
                    
                    grid[i][col] = 2
                    update(grid, i, col)
                    
                    # recursively treat the next column
                    helper(grid, col+1)
                    
                    # clean the grid before next iteration
                    grid = cleaned_grid
            
            return
        
        helper(grid, 0)
        return self.c
    
    # more efficient version. The idea remains the same
    # except that we gonna avoid the use of the update/clean
    # functions. First thing first we can reduce the grid to
    # a list of size n. The number at index i of the list
    # represents the col position of the queen in the ith row.
    # For example: 
    # [3, 1, 2, 0]
    # tell us:
    # Queen are in positions: (0,3), (1,1), (2, 2), (3,0)
    
    # That is a good thing, we reduce the memory from a grid
    # to a list. Now we want to replace the condition
    # if grid[i][col] != 1:
    # this condition used the fact that we update and clean
    # the grid in the previous solution.
    # this condition translates into
    # "if I can put a queen in i-row, col-column":
    # So we need a way to know if we can put a queen
    # in the i-row and col-column based on the list
    # this is what we will develop below
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.c = 0
        self.recur([-1]*n, row=0)
        return self.c
    
    def recur(self, arr, row):
        if row == len(arr):
            self.c += 1
            return
        
        for i in range(len(arr)):
            # put the queen in the list and check after
            arr[row] = i
            
            if self.allow(arr, row):
                self.recur(arr, row + 1)
        
        return
    
    # so we just need to define the allow function.
    # When can we say that we can put a queen in col
    # i knowing the list
    # as we put the queen in the list and check after
    # we already know that if the same value appear twice
    # in the list then this is not a good configuration
    # here having the same value twice in the list means
    # that the queen are on the same column
    # by construction we know that the queen cannot be on
    # the same line because we increment the row at each
    # iteration so we just need to check if they are queens
    # on the same diagonal, that is to say we need to check
    # that distance(y[queen_1] - y[queen_2]) != distance(x[queen_1] - x[queen_2])
    # by construction, again, x is the index in the list and y is the value
    # at the index, so we need to check that abs(arr[i] - arr[j]) != abs(j-i) = j-i
    def allow(self, arr, max_row):
        for i in range(max_row):
            if arr[max_row] == arr[i] or abs(arr[max_row] - arr[i]) == max_row - i:
                return False
        
        return True