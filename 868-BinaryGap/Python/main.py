class Solution:
    def binaryGap2(self, N):
        """
        :type N: int
        :rtype: int
        """
        maxi = 0
        prev_idx = -1

        while N:
            k = N & -N # get rightmost bit set to 1

            # Need to use log2
            idx = int(math.log2(k)) # get idx (position of the first 1)

            N = N & (N-1) # clear the rightmost set bit

            if prev_idx != -1 and (idx - prev_idx) > maxi:
                maxi = idx - prev_idx

            prev_idx = idx

        return maxi
    
    def binaryGap(self, N):
        prev, maxi = 0, 0
        
        for i, b in enumerate(bin(N)[2:]):
            if b == "0":
                continue
            
            maxi = max(maxi, i - prev)
            prev = i
        
        return maxi
        