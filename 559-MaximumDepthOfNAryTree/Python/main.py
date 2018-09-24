"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max = 0
        
        def helper(root, depth):
            if not root:
                return
            
            self.max = max(depth, self.max)
            
            for child in root.children:
                helper(child, depth+1)
        
        helper(root, 1)
        return self.max