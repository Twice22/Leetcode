# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        
        def helper(root, height=0):
            if not root:
                return 
            
            if len(res) <= height:
                res.append(-float("inf"))
            
            helper(root.left, height+1)
            helper(root.right, height+1)
            
            res[height] = max(root.val, res[height])
        
        helper(root)
        return res