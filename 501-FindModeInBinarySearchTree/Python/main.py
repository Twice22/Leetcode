# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        self.res = set()
        self.max_so_far = 1
        d = {}
        
        def helper(root):
            if not root:
                return
            
            d[root.val] = d.get(root.val, 0) + 1
            
            if d[root.val] > self.max_so_far:
                self.res = {root.val}
                self.max_so_far = d[root.val]
            elif d[root.val] == self.max_so_far:
                self.res.add(root.val)
                
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
                
        helper(root)
        
        return list(self.res)
    
    # without extra space we need to use 2
    # passes. One to find the maximum frequency
    # and one to go through the tree again and
    # store the node which appear maximum frequency times
    def findMode(self, root):
        # to count the maximum frequency we gonna make
        # use of the BST architecture of the tree, i.e we do
        # an inorder pass on the tree.. Doing that we are sure
        # that the values of the node will be traversed in a
        # sorted order. We also need to do that for the second
        # passe
        self.max = 1
        res = []
        def inOrderTraversal(root, prev, cur_max, version):
            if not root:
                return [prev, cur_max]
            
            prev, cur_max = inOrderTraversal(root.left, prev, cur_max, version)
            
            cur_max = cur_max + 1 if root.val == prev else 1
            if version == 0:
                self.max = max(self.max, cur_max)
            elif version == 1:
                if cur_max == self.max:
                    res.append(root.val)
            
            prev, cur_max = inOrderTraversal(root.right, root.val, cur_max, version)
            
            return [prev, cur_max]
        
        # populate self.max
        inOrderTraversal(root, None, 1, 0)
        inOrderTraversal(root, None, 1, 1)
        
        return res