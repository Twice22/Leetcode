class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        
        complement = set()        
        nodes = [root]
        
        while nodes:
            head = nodes.pop(0)
            
            if head.val in complement:
                return True
            complement.add(k-head.val)
            
            if head.right:
                nodes.append(head.right)
            if head.left:
                nodes.append(head.left)
        
        return False
            