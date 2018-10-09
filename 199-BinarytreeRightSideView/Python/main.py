# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        
        def helper(root, height):
            
            if height == len(res):
                res.append(root.val)
            
            if root.right:
                helper(root.right, height+1)
            
            if root.left:
                helper(root.left, height+1)
        
        helper(root, 0)
        return res