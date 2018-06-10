class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for word in strs: d["".join(sorted(word))].append(word)
        
        return list(d.values())