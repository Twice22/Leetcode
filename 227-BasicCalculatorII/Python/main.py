class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        pile = []
        a, b = "", ""
        i, size = 0, len(s)
        
        # recover first number
        while i < size and (s[i] == ' ' or s[i].isdigit()):
            a += s[i]
            i += 1
        
        a = a.strip()
        pile.append(a)
        
        while i < size:
            if s[i] == ' ':
                i += 1
                continue
            if not s[i].isdigit():
                sign = s[i]
                i += 1
                b = ''
                while i < size and (s[i] == ' ' or s[i].isdigit()):
                    b += s[i]
                    i += 1
                b = b.strip()
                if sign == '/' or sign == "*":
                    a = pile.pop()
                    b = str(int(a) // int(b) if sign == '/' else int(a) * int(b))
                    pile.append(b)
                else:
                    pile.append(sign)
                    pile.append(b)
               
        res = int(pile[0])
        for n in pile[1:]:
            if n == "+":
                sign = "+"
            elif n == '-':
                sign = '-'
            else:
                res = res - int(n) if sign == '-' else res + int(n)
            
        return res
                