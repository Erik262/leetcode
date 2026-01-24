#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#
from typing import List
# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        best_min = arrays[0][0]
        best_max = arrays[0][-1]
        res = 0

        for arr in arrays[1:]:
            max_min = abs(arr[-1] - best_min)
            min_max = abs(best_max - arr[0])

            res = max(res, max_min, min_max)

            best_min = min(best_min, arr[0])
            best_max = max(best_max, arr[-1])

        return res
# @lc code=end

