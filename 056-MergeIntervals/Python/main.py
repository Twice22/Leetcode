# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda u: u.start)
        a, b = intervals[0].start, intervals[0].end
        res = []
        for interval in intervals[1:]:
            aa, bb = interval.start, interval.end
            if aa <= b:
                b = max(bb, b)
            else:
                res.append(Interval(a, b))
                a, b = aa, bb

        res.append(Interval(a,b))
        
        return res