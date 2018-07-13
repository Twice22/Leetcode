class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        units = {1: "I", 5: "V", 10: 'X'}
        tenth = {1: "X", 5: "L", 10: "C"}
        centh = {1: "C", 5: "D", 10: "M"}
        thousands = {1 : "M"} # number are assumed to be in the range 0 - 3999
        
        d = {1: units, 10: tenth, 100: centh, 1000: thousands}
        
        key = 1
        res = ""
        
        while num:
            figure = num % 10
            num //= 10
            
            # same logic for uniths, tenth, centh...
            roman_digit = ""
            while figure:
                if figure == 9:
                    roman_digit += d[key][1] + d[key][10]
                    break
                elif figure == 4:
                    roman_digit += d[key][1] + d[key][5]
                    break
                
                if figure >= 5:
                    figure -= 5
                    roman_digit += d[key][5]
                else:
                    figure -= 1
                    roman_digit += d[key][1]
            
            key *= 10
            
            res = roman_digit + res
        
        return res
            
            
            
            
        