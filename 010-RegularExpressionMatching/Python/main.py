class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.size = len(s)
        rules = []
        i = len(p)-1
        while i >= 0:
            if i > 0 and p[i] == "*":
                rules = [(p[i-1], "*")] + rules
                i -= 2
            else:
                rules = [(p[i], "c")] + rules
                i -= 1
        
        return self.matching(s, rules, 0, {}) == len(s)
    
    def matching(self, s, rules, idx, d):
        key = str(idx) + "-" + str(len(rules))
        if key in d:
            return d[key]
    
        if not rules:
            return idx
            
        (letter, special), next_rules = rules[0], rules[1:]
        
        # case where we already matched the string
        # and the remaining rules doesn't have a "*"
        # then we already know it is not a match
        if idx >= self.size and special != "*":
            return -1
        
        nb_rules = "-" + str(len(next_rules))
        
        # if it's a character and no match return idx (i.e)
        # length of the current match
        if special == "c" and s[idx] != letter and letter != '.':
            return idx
        elif special == "c":
            res = self.matching(s, next_rules, idx+1, d)
            d[str(idx+1) + nb_rules] = res
            return res
        elif special == "*":
            r = [self.matching(s, next_rules, idx, d)]
            d[str(idx) + nb_rules] = r[-1] # don't forget case we don't match any character in the pattern "x*"
            while idx < self.size and (s[idx] == letter or letter == '.'):
                r.append(self.matching(s, next_rules, idx+1, d))
                d[str(idx+1) + nb_rules] = r[-1]
                idx += 1
            if not r:
                res = self.matching(s, next_rules, idx, d)
                d[str(idx) + nb_rules] = res
                return res
            else:
                return max(r)
                