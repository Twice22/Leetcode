class Solution:
    # O(n*m)
    def nextGreaterElement2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        size = len(nums2)
        
        for n1 in nums1:
            # search n1 in nums2
            for i, n2 in enumerate(nums2):
                if n2 == n1:
                    # if we find n1 in nums2
                    # find the next greatest number
                    j = i+1
                    while j < size and nums2[j] < n1:
                        j += 1
                    res.append(-1 if j == size else nums2[j])
                    break
        
        return res
    
    # O(n+m)
    def nextGreaterElement(self, nums1, nums2):
        # a better idea is to create the area of the next
        # biggest element of each number in nums2. To do so
        # let's work on an example:
        
        # [1, 4, 8, 5, 3, 2, 7]
        
        # starting from the end of the array
        # as 7 is the last element we will have (no biggest element at the right of 7)
        # [_, _, _, _, _, _, -1]
        
        # then for 2, just do:
        # 1. is 2 < 7 ? (n < x in the general case)
        # 2. is 2 < -1 ? (n < y in the general case)
        
        # if 1 is yes and 2 is no -> fill in with x
        # if 1 is yes and 2 is yes -> fill in with x 
        # (because x come from nums2 and so is the closest right number to n)
        # if 1 is no and 2 is yes -> fill in with y
        # if 1 and 2 are both no -> fill in with -1 if not better elts in the right of  nextGreater
        nextGreater = [-1]
        for i in range(len(nums2)-2, -1, -1):
            if nums2[i] < nums2[i+1]:
                nextGreater = [nums2[i+1]] + nextGreater
            elif nums2[i] < nextGreater[0]:
                nextGreater = [nextGreater[0]] + nextGreater
            else:
                for elt in nextGreater:
                    if elt == -1:
                        break
                    if elt > nums2[i]:
                        break
                
                if elt == -1:
                    nextGreater = [-1] + nextGreater
                else:
                    nextGreater = [elt] + nextGreater
        
        # print(nextGreater)
        # now construct a table from nums2 to have access to
        # the index of each element from its value
        d = {n:i for i, n in enumerate(nums2)}
        
        res = []
        for n in nums1:
            if n not in d:
                res.append(-1)
            else:
                res.append(nextGreater[d[n]])
        
        return res
        
        