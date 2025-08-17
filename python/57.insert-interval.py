from typing import List
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result


intervals = [[1,3],[4,6]] # [[1,6]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[9,10]] # [[1,2],[3,5],[6,7],[9,10]]
newInterval = [6,7]

print(Solution().insert(intervals, newInterval))
        
# @lc code=end

