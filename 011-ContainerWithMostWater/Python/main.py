class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        
        best_surface = 0
        max_height = 0
        
        ptr1, ptr2 = 0, len(height) - 1
        
        while ptr1 < ptr2:
            # took the min of the 2 height
            # and move the pointer
            if height[ptr1] > height[ptr2]:
                min_height = height[ptr2]
                ptr2 -= 1
            else:
                min_height = height[ptr1]
                ptr1 += 1
            
            # +1 to account for the fact that we have
            # already moved the pointer in the if conditions
            if min_height * (ptr2 - ptr1 + 1) > best_surface:
                best_surface = min_height * (ptr2 - ptr1 + 1)
        
        
        return best_surface