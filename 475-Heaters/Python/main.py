class Solution:    
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        radius = 0
        
        houses.sort()
        heaters.sort()
        
        heaters = [-float("inf")] + heaters + [float("inf")]
        
        i = 0
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            
            # we have     --- heaters[i] --- house --- heaters[i+1] --->
            cur_radius = min(house - heaters[i], heaters[i+1] - house)
            radius = max(radius, cur_radius)
        
        return radius