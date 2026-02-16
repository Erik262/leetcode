#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#
from typing import List
# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        prefix = [0] * n
        result = 0

        for i in range(n):
            prefix[i] = prefix[i-1] + nums[i]

        for i in range(n-1):
            left_sum = prefix[i]
            right_sum = total - left_sum

            if left_sum >= right_sum:
                result += 1

        return result
        
nums = [10,4,-8,7]

print(Solution().waysToSplitArray(nums))
# @lc code=end