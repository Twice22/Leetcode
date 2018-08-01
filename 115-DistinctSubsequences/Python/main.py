# step to find the solution of a dynamic programming
# problem. First come with the "naive" solution that
# compute over and over the same quantity several times
# and that leads a TLE (Time Limit Exceeded)
# See numDistinct1

# Then add a dictionary to this solution to avoid recomputing
# the same quantity over and over: this solution won't
# lead to a TLE: see numDistinct2

# Finally transform numDistinct2 into a bottom-up approach using
# an array (list): see numDistinct3

class Solution():
    # TLE
    def numDistinct1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # t substring of s.
        # how many substrings of s == t ?
        return self.count(s, t)
    
    def count(self, s, t):
        # base cases
        if not t:
            return 1
        
        if len(t) > len(s):
            return 0
        
        if len(t) == len(s) and t == s:
            return 1
        
        # general cases
        if t[0] == s[0]:
            return self.count(s[1:], t[1:]) + self.count(s[1:], t)
        else:
            return self.count(s[1:], t)
        
    # works but not fast
    def numDistinct2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # t substring of s.
        # how many substrings of s == t ?
        return self.count2(s, t, 0, 0, {})
    
    def count2(self, s, t, pos_s, pos_t, d):
        # we need to identify the position
        # of the first matching letters in t and s
        # (for example)
        key = str(pos_s) + "-" + str(pos_t)
        if key in d:
            return d[key]
        
        # base cases
        if not t:
            return 1
        
        if len(t) > len(s):
            return 0
        
        if len(t) == len(s) and t == s:
            return 1
        
        # general cases
        if t[0] == s[0]:
            val = self.count2(s[1:], t[1:], pos_s + 1, pos_t + 1, d) + \
            self.count2(s[1:], t, pos_s + 1, pos_t, d)
        else:
            val = self.count2(s[1:], t, pos_s + 1, pos_t, d)
        
        d[key] = val
        return val
    
    
    # finally bottom-up approach (translate numDistinct2)
    def numDistinct(self, s, t):
        size_string = len(s)
        size_target = len(t)
        
        dp = [0] * (size_target+1)
        dp[0] = 1 # base case: not t -> return 1
        
        # dp[j] = dp[j] if s[i] != t[j]
        # dp[j] = dp[j] + dp[j-1] if s[i] == t[j]
        
        for i in range(1, size_string + 1):
            for j in range(min(i, size_target), 0, -1):
                if s[i-1] == t[j-1]:
                    dp[j] += dp[j-1]
        
        return dp[-1]
    