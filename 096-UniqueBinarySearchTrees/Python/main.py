class Solution:
    def numTrees2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # actually we want to output how many BST stores values 1...n
        # Let f(i, n) be the number of BST that store 1...n with i as
        # a root then we have bst(n) = f(1, n) + f(2, n) + ... + f(n, n)
        # let's consider f(i,n): as we are looking for BST trees only
        # and as i is the root, it means that nodes 1 up to i-1 are on the
        # left of i and nodes i+1 up to n are on the right of i.
        # But as we are considering BST trees, it means that the left and
        # right sides should also be BST trees, so we have:
        # f(i, n) = bst(i-1) * bst(n-i) (nb of bst in the left times nb of bst
        # in the right hand side). So finally we can come up with this piece
        # of code (not to forget to cache the data!)
        return self.bst(n, {})
    
    def bst(self, size, seen):
        if size in seen:
            return seen[size]
        # base case: size = 1: 1
        if size == 0:
            return 1
        
        res = 0
        for i in range(1, size+1):
            res += self.bst(i-1, seen) * self.bst(size-i, seen)
        seen[size] = res
        return res
    
    
    # dynamic botttom-up approach (just translate
    # previous code iteratively using a list)
    def numTrees(self, n):
        # construct list of size n having bst(i) in index i:
        # initialize list with same base case as previously
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[-1]
        
        