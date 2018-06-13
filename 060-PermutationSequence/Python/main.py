class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 0 or n == 1:
            return "1"
        
        # to respect my definition
        k -= 1 
        nums = [i for i in range(1, n+1)]
    
        res = []

        partition = [1]
        for i in range(1, n-1):
            partition = [(i+1) * partition[0]] + partition

        for part in partition:
            idx = k // part

            res.append(nums[idx])
            del nums[idx]

            k = k % part

        res.append(nums[0])

        return "".join(list(map(str, res)))