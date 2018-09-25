class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # we are sure the given height and
        # width of the matrix is in range [1, 100]
        h = len(nums)
        w = len(nums[0])
        
        if r * c != h * w:
            return nums
        
        res = [[0] * c for _ in range(r)]

        y_, x_ = 0, 0
        for y in range(r):
            for x in range(c):                    
                res[y][x] = nums[y_][x_]
                
                x_ += 1
                if x_ == w:
                    x_ = 0
                    y_ += 1
        
        return res