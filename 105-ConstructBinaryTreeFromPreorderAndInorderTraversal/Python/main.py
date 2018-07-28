# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        val = preorder[0]
        del preorder[0]
        root = TreeNode(val)
        i = inorder.index(val)
        root.left = self.buildTree(preorder[:i], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i+1:])
        
        return root