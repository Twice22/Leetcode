class Solution(object):
    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if not s or len(s) <= 2:
            return s

        i, j = 0, len(s)-1
        while i <= j and s[i] != " ": i += 1
        while j > i and s[j] != " ": j -= 1

        rec = self.reverseWords(s[i: j+1])
        if not rec:
            if s[j+1:] == "" and s[:i] != "":
                return s[:i]
            if s[j+1:] != "" and s[:i] == "":
                return s[:i]
            return s[j+1:] + " " + s[:i]

        return  s[j+1:] + " " +  rec + " " + s[:i]
    
    def reverseWords(self, s):
        # pythonic easy solution
        return " ".join(s.strip().split()[::-1])