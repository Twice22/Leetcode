# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.build(root)
        return self.res
    
    def build(self, root):
        if not root:
            return []
        
        self.build(root.left)
        self.res.append(root.val)
        self.build(root.right)
    
    # iterative solution (more challenging)
    def inorderTraversal(self, root):
        if not root:
            return []
        
        pile = []
        node = root
        while node:
            pile.append(node)
            node = node.left
        
        res = []
        
        while pile:
            # print([x.val for x in pile])
            node = pile[-1]
            res.append(node.val)
            del pile[-1]            
            
            if node.right:
                pile.append(node.right)
                node = node.right
                while node.left:
                    pile.append(node.left)
                    node = node.left
            
        return res
            