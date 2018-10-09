# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        def helper(root):
            if not root:
                return 0, 0
            
            if not root.right and not root.left:
                return 0, root.val
            
            left = helper(root.left)
            right = helper(root.right)
            
            # if rob current house then return left + right + current house
            # else find max of left subtree, right subtree
            return max(left) + max(right), left[0] + right[0] + root.val
        
        
        return max(helper(root))