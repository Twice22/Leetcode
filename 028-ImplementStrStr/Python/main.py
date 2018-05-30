class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        
        size = len(haystack)
        matching_size = len(needle) - 1
        
        j = -1 # position current char in needle
        table = self.get_table(needle) 
        
        for i in range(size):
            while j > -1 and needle[j+1] != haystack[i]:
                j = table[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == matching_size:
                return i - matching_size
        
        return -1
    
    def get_table(self, needle):
        size = len(needle)
        table = [-1] * size
        j = -1
        
        for i in range(1, size):
            while j > -1 and needle[j + 1] != needle[i]:
                j = table[j]
            if needle[j + 1] == needle[i]:
                j += 1
            table[i] = j

        return table