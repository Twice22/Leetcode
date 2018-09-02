class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dictionary to keep track of freq of the elements
        freq = {}
        
        # dictionaries to keep track of a tuple of values that
        # indicates the first time a element occurs and the last time
        span = {}
        
        # keep track of the elements with the highest frequency
        max_elements = []
        max_freq = 0
        
        for i, n in enumerate(nums):
            freq[n] = freq.get(n, 0) + 1
            
            if n not in span:
                span[n] = [i, i]
            else:
                span[n][1] = i
            
            next_max_freq = max(max_freq, freq[n])
            
            if next_max_freq != max_freq:
                max_elements = [n]
            elif next_max_freq == freq[n]:
                max_elements.append(n)
                
            max_freq = next_max_freq
        
        # keep track of minium length of subarray
        min_length = math.inf
        
        for n in max_elements:
            min_length = min(min_length, span[n][1] - span[n][0] + 1)
        
        return min_length
            
        
        
            
            
            
        