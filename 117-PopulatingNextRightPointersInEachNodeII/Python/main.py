# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # slight variation of 116 solution
        # here the tree is not necessarily a perfect binary tree!
        
        # base cases
        if not root or \
           (root.left is None and root.right is None):
            return
        
        
        if root.left and root.right:
            root.left.next = root.right
        
        # the trick to connect 2 != subtree
        good_node = root.next
        while good_node and good_node.next and good_node.right is None and good_node.left is None:
            good_node = good_node.next
        if good_node:
            if root.right and good_node.left:
                root.right.next = good_node.left
            elif root.left and good_node.left:
                root.left.next = good_node.left
            elif root.right and good_node.right:
                root.right.next = good_node.right
            elif root.left and good_node.right:
                root.left.next = good_node.right
        
        # recursive call on subtree
        self.connect(root.right) # /!\ need to populate right tree before left
        self.connect(root.left)
        