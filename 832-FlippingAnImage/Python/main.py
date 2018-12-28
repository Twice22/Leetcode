class Solution:
    # inplace
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(A), len(A[0])
        for y in range(r):
            for x in range(math.ceil(c/2)):
                A[y][x], A[y][c-1-x] = 1-A[y][c-1-x], 1-A[y][x]
        
        return A
        
    
    def flipAndInvertImage2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-e for e in row[::-1]] for row in A]