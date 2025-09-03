from typing import List
import heapq

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key=lambda x: x.start)
        ends = []
        heapq.heapify(ends)
        heapq.heappush(ends, intervals[0].end)

        rooms = 1

        for i in range(1, len(intervals)):
            if intervals[i].start >= ends[0]:
                heapq.heapreplace(ends, intervals[i].end)
            else:
                heapq.heappush(ends, intervals[i].end)
            
            rooms = max(rooms, len(ends))
        return rooms


intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)] # 2
# intervals = [Interval(4, 9)] # 1

print(Solution().minMeetingRooms(intervals))