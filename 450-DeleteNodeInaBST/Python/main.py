# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        dummy = root
        prev = None
        
        while dummy:
            if key == dummy.val:
                break
                
            prev = dummy
            if key > dummy.val:
                dummy = dummy.right
            else:
                dummy = dummy.left
        
        if not dummy:
            return root
        
        # if leaf node
        if not dummy.left and not dummy.right:
            if not prev:
                return None
            elif prev.right == dummy:
                prev.right = None
            else:
                prev.left = None
        elif not dummy.right or not dummy.left:
            if not prev:
                return dummy.left if not dummy.right else dummy.right
            if prev.right == dummy:
                prev.right = dummy.left if not dummy.right else dummy.right
            else:
                prev.left = dummy.left if not dummy.right else dummy.right
        else: # inorder sucessor
            prev = dummy
            temp = dummy
            dummy = dummy.right
            while dummy.left:
                temp = dummy
                dummy = dummy.left
            
            prev.val = dummy.val
            if temp.right == dummy:
                temp.right = dummy.right
            else:
                temp.left = dummy.right
        
        return root
        