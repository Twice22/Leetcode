class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """     
        perm = [[nums[0]]]
        del nums[0]
    
        while nums:      
            elem = nums[0]
        
            perm_temp = []
        
            for i in range(len(perm[0])+1):
                for p in perm:
                    p_copy = p.copy()
                    p_copy.insert(i, elem)
                    perm_temp.append(p_copy)
        
            perm = perm_temp
        
            del nums[0]
    
        return perm