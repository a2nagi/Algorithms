# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)
        
        merged_lst = []
        for interval in intervals:
            if merged_lst == [] or merged_lst[-1].end < interval.start:
                merged_lst.append(interval)
            else:
                merged_lst[-1].end = max(merged_lst[-1].end, interval.end)
        return merged_lst
        
