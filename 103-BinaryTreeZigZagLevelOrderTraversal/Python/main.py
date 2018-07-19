# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        pile = [root]
        res = [[root.val]]
        order = -1
        
        while pile:
            new_pile = []
            for node in pile:
                if node.left:
                    new_pile.append(node.left)
                if node.right:
                    new_pile.append(node.right)
                
            if not new_pile:
                break            
            
            if order == 1:
                stack_it = [n.val for n in new_pile]
                order = -1
            else:
                stack_it = [n.val for n in reversed(new_pile)]
                order = 1
                
            res = res + [stack_it]
            
            pile = new_pile
        
        return res