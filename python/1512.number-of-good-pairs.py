#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
from typing import List
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            a = nums[i]

            for j in range(i, len(nums)):
                b = nums[j]

                if a == b and i < j:
                    res += 1

        return res

# @lc code=end

