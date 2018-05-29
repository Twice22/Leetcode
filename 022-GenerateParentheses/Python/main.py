class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.dfs(result, "", n, n)
        return result

    def dfs(self, result, text, leftParen, rightParen):

        if leftParen > rightParen:
            return

        if leftParen == 0 and rightParen == 0:
            result.append(text)
            return

        if leftParen > 0:
            self.dfs(result, text + '(', leftParen-1, rightParen)

        if rightParen > 0:
            self.dfs(result, text + ')', leftParen, rightParen-1)