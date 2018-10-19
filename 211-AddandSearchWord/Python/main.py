from collections import defaultdict

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        
        current["leaf"] = True

    def recsearch(self, word, node):
        if node == True:
            return False
        
        if len(word) == 0:
            return "leaf" in node
        
        res = False
        if word[0] == '.':
            for k in node.keys():
                res = res or self.recsearch(word[1:], node[k])
        elif word[0] in node:
            res = res or self.recsearch(word[1:], node[word[0]])
        
        return res
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.recsearch(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)