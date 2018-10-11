# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        # we can compute the mean using:
        # M(n+1) = n/(n+1) * [M(n) + V(n+1)/n]
        # where M(n) = sum V(i) for i=1..N
        
        if not root:
            return []
        
        nodes = [root]
        res = []
        
        while nodes:
            new_nodes = []
            
            mean = nodes[0].val
            c = 1
            
            for node in nodes:
                if node != nodes[0]:
                    mean = c/(c+1) * (mean + node.val / c)
                    c += 1
                
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            
            res.append(mean)
            nodes = new_nodes
        
        return res
                