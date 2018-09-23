class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.s = "." * n
        self.recur([-1]*n, row=0)
        return self.res
    
    def recur(self, arr, row):
        if row == len(arr):            
            self.res.append([self.s[:val] + "Q" + self.s[val+1:] for val in arr])
            return

        for i in range(len(arr)):
            arr[row] = i
            if self.allow(arr, row):
                self.recur(arr, row + 1)

        return

    def allow(self, arr, max_row):
        for i in range(max_row):
            if arr[max_row] == arr[i] or abs(arr[max_row] - arr[i]) == max_row - i:
                return False

        return True
                