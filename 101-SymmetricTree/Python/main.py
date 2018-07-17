# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self, arr):
        i, j = 0, len(arr) - 1
        while i < j and arr[i] == arr[j]:
            i += 1
            j -= 1
        
        return i >= j
    
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # iteratively
        if not root:
            return True
        
        nodes = [root]
        
        while nodes:
            new_nodes = []
            for node in nodes:
                if node:
                    new_nodes.append(node.left if node.left else None)
                    new_nodes.append(node.right if node.right else None)
            
            if not new_nodes:
                break
                  
            # check if there is symmetry at current depth
            arr = [n.val if n else None for n in new_nodes]
            if not self.check(arr):
                return False
                       
            nodes = new_nodes
            
        return True
    
    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.isSymRec(root.left, root.right)
    
    def isSymRec(self, left, right):
        if left is None and right is None:
            return True
        
        # we go in this case only if we don't go in the former
        # so naturally it means left is None AND right is not None
        # or the reverse
        if left is None or right is None:
            return False
        
        return left.val == right.val and self.isSymRec(left.right, right.left) and self.isSymRec(left.left, right.right)