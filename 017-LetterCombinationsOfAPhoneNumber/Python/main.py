class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ''
        }

        result = []
        currentSet = []

        digits = list(digits) # transform "23" into ['2', '3']

        self.dfs(digits, len(digits), currentSet, d, result)

        return result

    def dfs(self, digits, depth, currentSet, d, result):
        if depth == 0:
            result.append("".join(currentSet))
            return

        for pos_letter in d[digits[0]]:
            self.dfs(digits[1:], depth - 1, currentSet + [pos_letter], d, result)