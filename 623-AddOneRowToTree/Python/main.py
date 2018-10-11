class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        
        nodes = [root]
        h = 1
        
        while nodes:
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
                if h == d-1:
                    medium_node = TreeNode(v)
                    node.left, medium_node.left = medium_node, node.left
                    
                    medium_node = TreeNode(v)
                    node.right, medium_node.right = medium_node, node.right
                
            if h == d-1:
                break
            
            h += 1            
            nodes = new_nodes
        
        return root
            