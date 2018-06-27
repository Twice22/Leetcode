class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # need to modify inplace with O(1) extra memory
        # so we CANNOT use a dict and 2 passes
        if not nums:
            return 0
        
        ptr_insert, i, size = -1, 0, len(nums)
        
        while i < size:
            if ptr_insert != -1 and i != ptr_insert and ((i+1 < size and nums[i+1] != nums[i]) or i+1 >= size):
                nums[ptr_insert] = nums[i]
                ptr_insert += 1
            
            c = 1
            while i + 1 < size and nums[i+1] == nums[i]:
                c += 1
                i += 1
                if ptr_insert != -1 and i != ptr_insert and c <= 3:
                    nums[ptr_insert] = nums[i]
                    ptr_insert += 1
                if ptr_insert == -1 and c == 3:
                    ptr_insert = i
            
            # don't forget to add the last
            # "2 <=" proove we came from the while loop
            if ptr_insert != -1 and 2 <= c < 3:
                nums[ptr_insert] = nums[i-1]
                ptr_insert += 1
            
            # point on different next number
            i += 1
        
        return i if ptr_insert == -1 else ptr_insert