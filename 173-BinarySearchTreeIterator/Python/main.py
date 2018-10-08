# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stackLeft = []
        self.appendLeft(root)

    def appendLeft(self, node):
        while node:
            self.stackLeft.append(node)
            node = node.left
            
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stackLeft) > 0


    def next(self):
        """
        :rtype: int
        """
        node = self.stackLeft.pop()
        if node.right:
            self.appendLeft(node.right)
        return node.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())