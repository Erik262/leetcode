#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
from typing import List
# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}
        total = 0
        best = 0

        for i, num in enumerate(nums):
            if num == 0:
                total -= 1
            else:
                total += 1

            if total in first:
                best = max(best, i - first[total])
            else:
                first[total] = i

        return best
# @lc code=end

