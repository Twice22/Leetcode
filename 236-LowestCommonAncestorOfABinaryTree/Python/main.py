# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        res = [] # 1 if go right, 0 if go left
        
        nodes = [(root, "")]
        
        while nodes:
            node, s = nodes.pop(0)
            
            if node.val == p.val or node.val == q.val:
                res.append(s)
            
            if len(res) == 2:
                break
            
            if node.left:
                nodes = [(node.left, s + "0")] + nodes
            if node.right:
                nodes = [(node.right, s + "1")] + nodes
        
        s1, s2 = res
        for a, b in zip(s1, s2):
            if a != b:
                break
            if a == "0":
                root = root.left
            else:
                root = root.right

        return root