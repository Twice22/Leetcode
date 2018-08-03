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
    
    # better solution O(1) in space (otherwise easy to use
    # a while loop with a stack and an array but it is more
    # interesting to try more challenging thing)    
    def connect(self, root):
        # idea: let's assume we have:
        #      1
        #    /  \
        #   2    3
        #  / \  / \
        # 4  5  6  7
        #
        # in this configuration, we assume we are at
        # the root node: 1. Then as 1 as no parent that
        # has a right child we don't need to do anything (base case)
        # then we check if 1 has 2 children (it has 2 and 3) so we want
        # to connect 2 to 3, to do this we do:
        # root.left.next = root.right. Then after this pass we have:
        #
        #
        #      1
        #    /  \
        #   2 -> 3
        #  / \  / \
        # 4  5  6  7
        #
        # But no we want to connect 4 to 5, 5 to 6 and 6 to 7.
        # our current position is 2 for the left tree and 3 for the right tree
        # to handle the connection in the left tree it is easy (same opeation
        # as before: root.left.next = root.right)
        # idem for the right tree! 
        # Now, the trick is: how to handle the connection between 5 and 6?
        # Well, the idea is that their is a bridge between 2 and 3 (2 -> 3)
        # due to our previous operation so we just need to connect:
        # root_from_left_tree.right.next = root_from_left_tree.next.left
        # where in our example root_from_left_tree is the node having value 2!
        # let's write the algorithm:
        
        # base case
        if not root or \
           (root.left is None and root.right is None):
            return
        
        # else, has we assume a perfect binary tree no need
        # to check if root.left and root.right are not None
        root.left.next = root.right
        
        # the trick to connect 2 != subtree
        if root.next:
            root.right.next = root.next.left
        
        # recursive call on subtree
        self.connect(root.left)
        self.connect(root.right)
        
    
    def connect2(self, root):
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