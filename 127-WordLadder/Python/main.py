class Solution:    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        # we assume all the words have same
        # size so we just need to get the size
        # once and for all
        size = len(beginWord)
        curWords = {beginWord}
        endWords = {endWord}

        # recall which values we already seen
        seen = set()
        c = 1


        while curWords:
            
            # use 2-end BFS. Next expand of the node will
            # be on the set that contains fewer nodes
            if len(curWords) > len(endWords):
                curWords, endWords = endWords, curWords

            nextWords = set()
            for possible_word in curWords:

                # change one letter of each parent word
                for i in range(size):
                    for letter in alphabet:
                        child_word = possible_word[:i] + letter + possible_word[i+1:]

                        # early stopping
                        if child_word in endWords:
                            return c + 1

                        if child_word not in seen and child_word in wordSet:
                            seen.add(child_word)
                            nextWords.add(child_word)

            # iterate BFS
            curWords = nextWords
            c += 1

        return 0