class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Well we can do that in O(n)
        # just add first element of array to last element of array:
        # if numbers[0] + numbers[-1] > target then
        # compute n = numbers[0] + numbers[-2]. if n < target this time
        # then compute numbers[1] + numbers[-2] and so on...
        # so we just need 2 pointers and we move one of those pointers
        # at each iteration
        i, j = 0, len(numbers)-1
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
            
        return [i+1, j+1] # not zero-based index