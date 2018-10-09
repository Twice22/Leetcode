# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binarySearch(self, root, lower, upper):
        dummy = root
        while lower <= upper:
            
            mid = (lower + upper) // 2
            s = bin(mid)[3:]
            terminate = False
            
            for letter in s:
                try:
                    if letter == "1":
                        dummy = dummy.right
                    else:
                        dummy = dummy.left
                except:
                    terminate = True
                    break
            
            if terminate or dummy is None:
                upper = mid-1
            else:
                lower = mid+1
            
            dummy = root
        
        return upper            
            
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # can do a binary search
        
        if not root:
            return 0
        
        # retrieve lower and upper limits
        h = 0
        dummy = root
        while dummy:
            dummy = dummy.right
            h += 1
        
        power = (1 << h)
        lower, upper = power - 1, 2 * power - 1
        c = self.binarySearch(root, lower, upper)
        
        return c
        
        