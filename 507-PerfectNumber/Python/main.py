class Solution:
    def checkPerfectNumber2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        limit = math.ceil(num**0.5)
        total = 0
        for n in range(2,limit):
            if num % n == 0:
                total += n + num // n
        
        return total+1 == num
    
    # fct that uses the result from the
    # wikipedia page https://fr.wikipedia.org/wiki/Nombre_parfait
    import bisect
    def checkPerfectNumber(self, num):
        # note: 11 which is prime is not in the list!
        primers = [2, 3, 5, 7, 13] # 17, 19
        for i, p in enumerate(primers):
            primers[i] = (1 << (p - 1)) * ((1 << p) - 1)
        
        idx = bisect.bisect_left(primers, num)
        return idx < len(primers) and num == primers[idx]