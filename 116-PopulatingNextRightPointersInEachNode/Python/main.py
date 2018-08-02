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
        head = root
        
        def helper(left, right):
            if not left or not right:
                return
            
            left.next = right
            
            helper(left.left, left.right)
            helper(right.left, right.right)
            helper(left.right, right.left)
        
        if not root:
            return
        
        helper(root.left, root.right)
        root = head