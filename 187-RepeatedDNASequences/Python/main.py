class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        
        subseq = s[:10]
        d = {subseq: 1}
        res = []
        
        for letter in s[10:]:
            subseq = subseq[1:] + letter               
            if subseq in d and d[subseq] == 1:
                res.append(subseq)
            d[subseq] = d.get(subseq, 0) + 1
        
        return res
                