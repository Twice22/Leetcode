class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def buildTree(nums):
            if not nums:
                return None
            
            max_idx, max_val = max(enumerate(nums), key=lambda x: x[1])
            root = TreeNode(max_val)
            
            root.left = buildTree(nums[:max_idx])
            root.right = buildTree(nums[max_idx+1:])
            
            return root
        
        return buildTree(nums)
        