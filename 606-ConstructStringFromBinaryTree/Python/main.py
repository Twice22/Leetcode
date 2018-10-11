class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """        
        def helper(t):
            if not t:
                return ""
            
            if not t.left and not t.right:
                return str(t.val)
            
            left = "(" + helper(t.left) + ")"
            temp = helper(t.right)
            right = "" if temp == "" else "(" + temp + ")"
            
            return str(t.val) + left + right
        
        return helper(t)