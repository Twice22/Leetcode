class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        idx = 0
        s = 0
        size = len(gas)
        gas_in_tank_so_far = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            consume = g - c
            
            # gas available in the car so far
            gas_in_tank_so_far += consume
            
            if gas_in_tank_so_far < 0:
                # we are sure that indexes from last idx to i are
                # not good indexes because if idx+j to i are a good
                # available index it means that sum(idx+j ...i) > sum(idx ... i)
                # that is to say sum(idx ... idx+j) < 0 and it is not possible
                # because we would have enter the if statement
                idx = (i + 1) % size
                gas_in_tank_so_far = 0
                
            s += consume
                
        return idx if s >= 0  else -1 
        
        