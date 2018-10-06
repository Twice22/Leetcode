class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d1, d2 = {}, {}
        bulls, cows = 0, 0
        for l1, l2 in zip(secret, guess):
            if l1 == l2:
                bulls += 1
            else:
                d1[l1] = d1.get(l1, 0) + 1
                d2[l2] = d2.get(l2, 0) + 1
        
        for k, v in d2.items():
            if k in d1:
                cows += min(d1[k], v)
        
        return str(bulls) + "A" + str(cows) + "B"