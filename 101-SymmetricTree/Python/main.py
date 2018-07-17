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
    
    def isSymmetric(self, root):
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
                
        