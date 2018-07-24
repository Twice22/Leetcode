class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        max_profit = 0
        min_so_far = prices[0]
        for price in prices[1:]:
            if price > min_so_far:
                max_profit = max(price - min_so_far, max_profit)
            else:
                min_so_far = price
        
        return max_profit