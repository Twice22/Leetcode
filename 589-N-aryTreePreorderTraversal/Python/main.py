"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        nodes = [root]
        res = []
        
        while nodes:
            
            new_nodes = []
            
            if nodes[0].children:
                for child in nodes[0].children:
                    new_nodes.append(child)
            
            head = nodes.pop(0)
            res.append(head.val)
            
            nodes = new_nodes + nodes
        
        return res