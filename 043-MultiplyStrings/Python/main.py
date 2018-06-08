class Solution:
    def __init__(self):
        self.d = {str(i): i for i in range(0, 10)}
        self.s = {i: str(i) for i in range(0, 10)}
    
    def multiply_by_figure(self, num1, digit):
        str_res = ""
        digit = self.d[digit]
        carry = 0

        for letter in num1[::-1]:
            mult = self.d[letter] * digit + carry
            carry = mult // 10
            current_digit = mult % 10
            str_res = self.s[current_digit] + str_res

        if carry:
            str_res = self.s[carry] + str_res

        return str_res
    
    def add(self, num1, num2):
        if len(num1) > len(num2):
            return self.add(num2, num1)

        # num1 less figure
        size1, size2 = len(num1)+1, len(num2)+1
        carry = 0
        str_res = ""
        for i in range(1, size1):
            add = self.d[num1[-i]] + self.d[num2[-i]] + carry
            carry = add // 10
            current_digit = add % 10
            str_res = self.s[current_digit] + str_res

        for j in range(size1, size2):
            add = self.d[num2[-j]] + carry
            carry = add // 10
            current_digit = add % 10
            str_res = self.s[current_digit] + str_res

        if carry:
            str_res = self.s[carry] + str_res

        return str_res
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        
        if len(num1) > len(num2):
            return self.multiply(num2, num1)
        
        # num1 is smaller number
        total_sum = "0"
        
        for i, figure in enumerate(num1[::-1]):
            term = self.multiply_by_figure(num2, figure) + "0" * i
            total_sum = self.add(term, total_sum)
        
        return total_sum
        