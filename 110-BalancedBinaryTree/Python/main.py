# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        diff = [True]
        
        self.balRec(root, diff)
        
        return diff[0]
    
    def balRec(self, root, diff):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0
        
        if root.left and not root.right or \
           root.right and not root.left:
            gap = self.balRec(root.right if root.right else root.left, diff) + 1
            if gap > 1:
                diff[0] = False
            return gap
        
        right = self.balRec(root.right, diff) + 1
        left = self.balRec(root.left, diff) + 1
        gap = max(right, left)
        if abs(right-left) > 1:
            diff[0] = False
        return gap
        
        
            