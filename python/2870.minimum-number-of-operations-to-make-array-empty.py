#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        result = 0

        for value in cnt.values():
            if value == 1:
                return -1

            result += (value + 2) // 3

        return result
# @lc code=end

