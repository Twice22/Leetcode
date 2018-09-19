class Solution:
    def getDigit(self, position, range):
        # examples
        # 47th number in the range [10, 99]:
        # is the number a tenth or a unit ? -> 47 % 2 (nb of digits in the range) == 1
        # so the number is a tenth (unit = 0, tenth = 1) and 47 // 2 = 23
        # so the number is the 23th tenth in the range [10, 99]: (10 + 23) // 10 = 3 % 10 == 3
        
        # 144th number in the range [100, 999]:
        # is the number a centh, tenth or a unit ? -> 144 % 3 (nb of digits in the range) == 0
        # so the number is a unit (unit = 0, tenth = 2, centh = 1) and 144 // 3 = 48
        # so the number is the 48th unit in the range [100, 999]
        # the first unit being a 0 it is (48 - 1) % 10 = 7
        
        # 290th number in the range [100, 999]:
        # is the number a centh, tenth or a unit ? -> 290 % 3 (nb of digits in the range) == 2
        # so the number is a tenth (unit = 0, tenth = 2, centh = 1) and 290 // 3 = 96
        # so the number is the 96th tenth we encounter in the range [100, 999]
        # (100 + 96) // 10 == 19 % 10 (keep last digit) = 9
        length = len(str(range))
        digit = position % length
        positionalDigit = position // length
        if digit == 0: # unit
            return (positionalDigit - 1) % 10
        
        return ((range + positionalDigit) // (10**(length-digit))) % 10
            
            
    
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # base case
        if n <= 9:
            return n
        
        # handle other cases:
        # 10 - 99 -> 10*2*9 digits
        # 100 - 999 -> 100*3*9 digits
        # 1000 - 9999 -> 1000*4*9 digits ...
        # need to find which case are we in...
        # examples:
        # 56 : (9 digits from 1 - 9) - rest: (56-9) = 47th number in the range [10, 99]
        # 333 : (9 digits from 1 - 9 + 180) + (180 from 10 - 99) - rest: 333-180-9 = 144th number in the range [100, 999]
        span = 2
        limit = 9
        max_range = 10
        prev_limit = 0
        while n > limit:
            prev_limit = limit
            limit += max_range*span*9
            span += 1
            max_range *= 10
        
        return self.getDigit(n - prev_limit, max_range // 10)
            
        
        
        