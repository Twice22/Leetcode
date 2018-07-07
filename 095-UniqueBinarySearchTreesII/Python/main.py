# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        
        return self.generate(1, n)
    
    def generate(self, beg, end):
        if beg > end:
            return [None]
        
        trees = []
        for i in range(beg, end+1):
            left = self.generate(beg, i-1)
            right = self.generate(i+1, end)
            for j in range(len(left)):
                for k in range(len(right)):
                    root = TreeNode(i)
                    root.left = left[j]
                    root.right = right[k]
                    trees.append(root)
        return trees
            