# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and not q:
            return False
        elif q and not p:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val