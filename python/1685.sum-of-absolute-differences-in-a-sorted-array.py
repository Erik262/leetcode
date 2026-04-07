#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#

from typing import List
# @lc code=start
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        left_sum = 0
        n = len(nums)
        result = []

        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            left = num * i - left_sum
            right = right_sum - num * (n - i - 1)
            result.append(left + right)
            left_sum += num

        return result

nums = [2,3,5] # [4,3,5]
print(Solution().getSumAbsoluteDifferences(nums)) 
# @lc code=end

