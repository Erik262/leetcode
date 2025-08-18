from typing import List
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x : x[0])
        merged = []

        for s, e in intervals:
            if not merged or s > merged[-1][1]:
                merged.append([s,e])
            else:
                merged[-1][1] = max(e, merged[-1][1])

        return merged

intervals = [[1,3],[1,5],[6,7]] # [[1,5],[6,7]]
intervals = [[1,2],[2,3]] # [[1,3]]
intervals = [[1,3],[2,6],[8,10],[15,18]]

print(Solution().merge(intervals))
        
# @lc code=end

