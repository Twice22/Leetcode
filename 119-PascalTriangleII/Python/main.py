class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        arr = [1]
        
        for i in range(rowIndex):
            arr = [1] + [arr[i-1]+arr[i] for i in range(1, len(arr))] + [1]
        
        return arr
        