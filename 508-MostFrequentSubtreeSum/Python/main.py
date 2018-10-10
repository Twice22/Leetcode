# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = {}
        self.max_freq = 0
        res = []
        
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            sum = left + right + root.val
            d[sum] = d.get(sum, 0) + 1
            
            if d[sum] > self.max_freq:
                self.max_freq = d[sum]
                res.clear()
                res.append(sum)
            elif d[sum] == self.max_freq:
                res.append(sum)
            
            return sum
            
        helper(root)
        return res