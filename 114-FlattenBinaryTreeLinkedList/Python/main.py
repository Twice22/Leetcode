# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        # idea is to put the rightmost part of the tree
        # beneath the second to last rightmost part of the tree:
        #     1
        #    / \
        #   2   5
        #  / \   \
        # 3   4   6
        
        # become:
        # 1
        #  \ 
        #   2 
        #  / \ 
        # 3   4 
        #      \
        #       5
        #        \
        #         6
        
        # then root = root.right (2) then we keep going
        
        while root:
            if root.left:
                second_right_most = root.left
                # take the second to last rightmost part of the tree
                while second_right_most.right:
                    second_right_most = second_right_most.right
                
                # add the rightmost part of the tree beneath the second
                # to last rightmost part of the tree
                second_right_most.right = root.right
                
                # put the left part of the tree to the right part
                # and nullify the left part
                root.right = root.left
                root.left = None
                
            # then move the root to the next element (2) in our example
            root = root.right
        
    
    
    def flatten2(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            root = None
        else:
            res = [root.val]

            def helper(root):
                if not root:
                    return

                if root.left:
                    res.append(root.left.val)
                    helper(root.left)

                if root.right:
                    res.append(root.right.val)
                    helper(root.right)

            helper(root)
            root.left = None
            head = root
            for n in res[1:]:
                root.right = TreeNode(n)
                root = root.right

            root = head
            
                
            