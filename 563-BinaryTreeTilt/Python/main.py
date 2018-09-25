# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        
        def helper(root):           
            left, right = 0, 0
            if root.left:
                left = helper(root.left)
            
            if root.right:
                right = helper(root.right)
            
            self.res += abs(left - right)
            
            return left + right + root.val
        
        if not root:
            return 0
        
        helper(root)
        return self.res