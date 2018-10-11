# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.leftmost = root.val
        self.max = 0
        
        def bfs(root, h=0):
            if not root:
                return
            
            if not root.right and not root.left:
                if h > self.max:
                    self.leftmost = root.val
                    self.max = h
                return
            
            bfs(root.left, h+1)
            bfs(root.right, h+1)
        
        bfs(root)
        return self.leftmost