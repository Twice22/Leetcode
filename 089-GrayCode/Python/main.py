class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]

        for it in range(0, n):
            add = 1 << it
            size = len(res)

            for j in range(size):
                res.append(res[size-1-j] + add)

        return res