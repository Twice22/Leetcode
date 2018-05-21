import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return float(0.0)
        
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        # at this point len(nums1) <= len(nums2)
        size_1 = len(nums1)
        size_2 = len(nums2)
        
        beg = 0
        end = size_1

        while beg <= end:
            mid1 = (end + beg) // 2
            
            # mid2 is the complementary of mid1 so that
            # mid1 + mid2 = median of the array that we would
            # have obtained if we had merged nums1 and nums2
            mid2 = (size_1 + size_2 + 1) // 2 - mid1
            
            # get maximum of left partition of nums1, if no element max = -inf
            maxLeftNums1 = -math.inf if mid1 == 0 else nums1[mid1 - 1]
            
            # get minimum of right partition of nums1
            # if all elements in left partition: min = +inf
            minRightNums1 = math.inf if mid1 == size_1 else nums1[mid1]
            
            # get maximum of left partition of nums2
            # if no element in left partition: max = -inf
            maxLeftNums2 = -math.inf if mid2 == 0 else nums2[mid2-1]
            
            # get min of right partition of nums2
            # if all element in left partition: min = +inf
            minRightNums2 = math.inf if mid2 == size_2 else nums2[mid2]
            
            # if max of elements in left partition of nums1
            # < min of elements in right partition of nums2
            # and max of elements in left partition of nums2
            # < min of elements in right partition of nums1
            # then it means all the elements in the left part 
            # < all elements in the right part
            if (maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1):
                if (size_1 + size_2) % 2 == 0:
                    # if len of "merge" array is even then return the
                    # mean of (max of left part + min of right part)
                    return float((max(maxLeftNums1, maxLeftNums2) + \
                            min(minRightNums1, minRightNums2)) / 2)
                else:
                    # return max of left part
                    return float(max(maxLeftNums1, maxLeftNums2))
            elif maxLeftNums1 > minRightNums2:
                # then we need to decrease mid1 by dichotomic search
                end = mid1 - 1
            else:
                # need to increase mid1
                beg = mid1 + 1
            
        return float(0)
        
            