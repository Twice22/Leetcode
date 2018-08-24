class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for ls, lt in zip(s, t):
            s_dict[ls] = s_dict.get(ls, 0) + 1
            s_dict[lt] = s_dict.get(lt, 0) - 1
        
        return not any(s_dict.values())