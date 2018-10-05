class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """        
        return [e for e in range(left, right+1) if self.isSelfDividing(e)]
    
    def isSelfDividing(self, num):
        if num % 10 == 0:
            return False
        
        n = num
        while num:
            if num % 10 == 0 or n % (num % 10) != 0:
                return False
            num = num // 10
        
        return True