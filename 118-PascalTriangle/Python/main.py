class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        
        arr = [[1]]
        
        for _ in range(numRows-1):
            last = arr[-1]
            new_arr = [1] + [last[i-1] + last[i] for i in range(1, len(last))] + [1]
            arr.append(new_arr)
        
        return arr