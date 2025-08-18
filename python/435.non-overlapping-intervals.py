from typing import List
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        end_keep = intervals[0][1]
        removal = 0

        for s, e in intervals[1:]:

            if s >= end_keep:
                end_keep = e
                continue

            if s < end_keep:
                removal += 1

        return removal







intervals = [[1,2],[2,4],[1,4]] # 1
intervals = [[1,2],[2,4],[1,4],[1,5]] # 2
intervals = [[1,2],[2,4]] # 0
intervals = [[1,100],[11,22],[1,11],[2,12]] # 2

print(Solution().eraseOverlapIntervals(intervals))

        
# @lc code=end

