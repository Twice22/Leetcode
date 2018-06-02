class Solution:
    def __init__(self):
        self.integers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        self.d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        self.max_int = (1 << 31) - 1
        self.min_int = -(1 << 31)
    
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == "":
            return 0
        
        sign = 1
        size = len(str)
        i = 0
        
        # check whitespaces
        while i < size and str[i] == ' ': i += 1
        
        if i == size:
            return 0
        
        # check +/- sign
        if str[i] == "+" or str[i] == '-':
            sign = 1 if str[i] == "+" else -1
            i += 1
        elif str[i] not in self.integers:
            return 0
        
        beg = i        
        while i < size and str[i] in self.integers: i += 1
        
        number = str[beg:i]
        
        # convert string to number
        res = 0
        for figure in number:           
            res = self.d[figure] + res * 10
        
        result = sign * res
        
        return max(min(result, self.max_int), self.min_int)