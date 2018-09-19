class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # we just need to find the divisor of area
        # that is the closest to sqrt(area) ....
        # lets assume we find the closest divisor of area
        # nearest to sqrt(area) and lower than sqrt(area)
        # than this number will be W and the number that
        # multiply W to get area will be L...
        pivot = int(math.sqrt(area))
        for i in range(pivot, -1, -1):
            if area % i == 0:
                return [area // i, i]
        
        return [0, 0]