# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        
        def helper(root, sum, path):
            if root and not (root.left or root.right) and sum == root.val:
                res.append(path + [root.val])
                return
            
            if not root:
                return
            
            helper(root.left, sum - root.val, path + [root.val])
            helper(root.right, sum - root.val, path + [root.val])
                
        helper(root, sum, path)
        return res