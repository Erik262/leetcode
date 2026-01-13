#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#
from typing import List
# @lc code=start
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)

        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
# @lc code=end

