# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        pile = [root]
        res = [[root.val]]
        
        while pile:
            new_pile = []
            for node in pile:
                if node.left:
                    new_pile.append(node.left)
                if node.right:
                    new_pile.append(node.right)
                
            if not new_pile:
                break            
            
            stack_it = [n.val for n in new_pile]
            res = res + [stack_it]
            
            pile = new_pile
        
        return res