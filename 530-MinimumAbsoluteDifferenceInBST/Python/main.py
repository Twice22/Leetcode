# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # as it is a binary search tree if we
        # browse the tree with an inorder traversal
        # we will see the node in sorted order
        # so we just need to take the min of the previous
        # seeing node and the current node.
        # We can do that with O(1) space like this:
        self.min = float("inf")
        
        def inOrderTraversal(root, prev):
            if not root: return prev
            
            prev = inOrderTraversal(root.left, prev)
            self.min = min(self.min, abs(root.val-prev))
            prev = inOrderTraversal(root.right, root.val)
            return prev
        
        inOrderTraversal(root, -float("inf"))
        return self.min