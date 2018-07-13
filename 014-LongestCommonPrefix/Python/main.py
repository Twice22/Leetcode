class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for word in strs[1:]:
            for i, l in enumerate(prefix):
                if i == len(word) or l != word[i]:
                    prefix = prefix[:i]
                    break
        
        return prefix
                