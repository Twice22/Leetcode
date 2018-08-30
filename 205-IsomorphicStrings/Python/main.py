class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # we assume s and t has same length
        # so we don't need to check that
        
        d1, d2 = {}, {}
        for l1, l2 in zip(s, t):
            if l1 not in d1:
                d1[l1] = l2
            elif d1[l1] != l2:
                return False
            if l2 not in d2:
                d2[l2] = l1
            elif d2[l2] != l1:
                return False
        
        return True