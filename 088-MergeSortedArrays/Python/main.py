class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # the idea is to beginning where there is space,
        # that is to say where there are the extra zeroes.
        # so we will sort it by checking that the last number of nums2
        # is less or equal to the last number of nums1
        
        if n == 0:
            return
        
        size = m+n-1
        m -= 1
        n -= 1
        
        for i in range(size, -1, -1):
            if nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1

            if m == -1:
                if n >= 0:
                    nums1[:i] = nums2[:i]
                break
            if n == -1:
                break