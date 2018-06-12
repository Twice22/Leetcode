class Solution:
    # TLE solution (just to remember the first naive idea)
    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True

        size = len(nums)

        accessible_cases = [False] * size
        accessible_cases[-1] = True

        for i in range(size-2, -1, -1):
            for j in range(min(i+nums[i], size-1), i-1, -1):
                if accessible_cases[j] == True:
                    accessible_cases[i] = True
                    break

        return accessible_cases[0] == True

    # fastest idea !
    def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True

    size = len(nums)
    distance = 1
        
    for i in range(size-2, -1, -1):
        # if we can reach all the cases from i to i + nums[i]
        # then at the next iteration we need to be able to reach
         # index i that is to say to reach at least a distance of 1:
        # distance = 0 and distance += 1 make it == 1
        if nums[i] >= distance:
            distance = 0
        # if nums[i] <= distance then we increment the distance by
        # one and continue looping, hoping tha at a certain index
        # nums[i] > distance
        distance += 1
        
    # we can reach the end of the array if nums[0] > distance
    # because distance is updated at each iteration
    return nums[0] >= distance