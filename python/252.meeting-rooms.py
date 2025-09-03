from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_end = float("-inf")
        intervals = sorted(intervals, key=lambda x: x.start)

        for interval in intervals:
            if interval.start < prev_end:
                return False
            else:
                prev_end = interval.end

        return True

intervals = [(0,30),(5,10),(15,20)] # False
intervals = [(5,8),(9,15)] # True
interval = Interval(intervals)
print(Solution().canAttendMeetings(interval))