class Solution:
    
    def longestConsecutive3(self, nums):
        d = {}
        
        max_length = 0
        
        for n in nums:
            # if current element (n) has already been seen
            # then d[n] != 0 and so we just continue looping
            # if n is an element in the middle of a sequence then
            # d[n] can be any number != 0 (1).
            # if d[n] is a element at the extremity of a sequence
            # then d[n] should contain the length of the sequence
            # this is what we do in the rest of the code
            if n in d and d[n]:
                continue
            
            
            # if no adjacent sequence to n (i.e (n-1) and (n+1)
            # are both not in d) then update d[n] to be 1
            # (length of the seq SO FAR == 1) and update the max so far
            if (n-1) not in d and (n+1) not in d:
                d[n] = 1
                max_length = max(max_length, 1)
                continue
            
            
            # if at current iteraiont, (n-1) is not in d
            # due to the previous if statement it means (n+1)
            # is in d. two cases:
            # - their is a sequence starting with n (if (n-1) doesn't
            #   appear in the rest of the number we yet didn't loop thru)
            # - their is a sequence containing n (that is to say both
            #   (n+1) and (n-1) appear in the sequence but (n-1) as not yet
            #   been seen)
            if (n-1) not in d:
                # so here we know n either starts a sequence or is part
                # of a sequence. what we want to do is to update the
                # extremity of the sequence so far (up to the current iteration)
                # such that d[left_extremity] = d[right_extremity]
                # = number of element in the sequence so far
                
                # if we enter this loop at the current iteration then it means
                # that AT THE CURRENT ITERATION, n = left_extremity (because (n-1)
                # is not in the dictionary d at the current iteration)
                # and (n+d[n+1]) = right_extremity.
                # Indeed. let's imagine the following input array:
                # [-2, -3, ..., -4]
                # then the algorithm will do:
                # first iteration: d = {-2: 1}
                # 2nd iteration: d = {-2: 2, -3: 2} (the extremity of the current sequence = length of the current sequence)
                # 3rd iteration: d = {-4: 3, -3: 2, -2: 3}, so here n = -4 = left_extremity
                # and right_extremity = -2 = n + d[n+1] = -4 + d[-4+1] (because (n+1) exists so far) = -4 + d[-3] = -2
                # because d[-3] contains the length of the sequence so far

                r = d[n+d[n+1]] = d[n] = d[n+1] + 1
                
                # then we update the maximum length to be
                # the max we get at the previous iteration and the
                # max we compute at the current iteration
                max_length = max(max_length, r)
                continue
            
            # same idea if we already saw (n-1) before n...
            if (n+1) not in d:
                r = d[n-d[n-1]] = d[n] = d[n-1] + 1
                max_length = max(max_length, r)
                continue
            
            # else: (n-1) and (n+1) have been seen before n
            # then according to the previous if statements d[n-1] contains
            # the length of the sequence finishing by (n-1) and d[n+1]
            # contains the length of the sequence beginning by (n+1)
            # so the length of the sequence up to the current
            # iteration is actuall: d[n-1] + d[n+1] + 1
            # and we need to update the left_extremity and the right_extremity
            # of the current sequence. here
            # left_extremity = n-d[n-1] and right_extremity = n+d[n+1]
            # and so the following code...
            # Note: don't forget to mark d[n] so that d[n] != 0
            # that is to say don't forget to add d[n] = ...
            r = d[n] = d[n-d[n-1]] = d[n+d[n+1]] = d[n-1] + d[n+1] + 1
            max_length = max(max_length, r)
        
        return max_length
    
    # not very aesthetic solution
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # transform to set. Avoid duplicate and O(1) to
        # find an element in the set
        nums = set(nums)
        
        # save max_length
        max_length = 0
        
        for n in nums:
            if (n-1) not in nums:
                y = 1
                while (n+y) in nums:
                    y += 1
                max_length = max(max_length, y)
        
        return max_length