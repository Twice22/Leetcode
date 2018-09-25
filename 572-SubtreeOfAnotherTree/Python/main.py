class Solution:
    def isSame(self, s, t):        
        if not t and not s:
            return True
        
        if (not t) or (not s):
            return False
        
        # we are sure t and s exit if
        # we reach here
        return t.val == s.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        if not t and not s:
            return True
        
        if not t:
            return False
        
        if (not t) or (not s):
            return False        
        
        if s.val == t.val:
            if self.isSame(s, t):
                return True
            else:
                return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)