from typing import List
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

nums = [2,-3,4,-2,2,1,-1,4] # 8
# nums = [-1] # -1

print(Solution().maxSubArray(nums))
# @lc code=end

