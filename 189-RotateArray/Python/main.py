class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        c = 0 # count number of assignments
        
        for i in range(k):
            j = i
            temp = nums[j]
            
            while True:
                next_ptr = (j + k) % size
                
                # if we loop through all the elts of
                # the array and go back to the starting pt
                # need to break and proceed from the next element
                if next_ptr == i:
                    break
                
                temp, nums[next_ptr] = nums[next_ptr], temp                
                j = next_ptr
                c += 1
            
            nums[next_ptr] = temp
            c += 1
            
            if c == size:
                break
        
                