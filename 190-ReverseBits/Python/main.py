class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x = 0
        for _ in range(32):
            x = x << 1
            x |= (n & 1)

            n = n >> 1

        return x