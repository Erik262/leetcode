#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#
from typing import List
# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr_zero = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr_zero += 1
                result += curr_zero
            else:
                curr_zero = 0

        return result

    
nums = [1,3,0,0,2,0,0,4] # 6

print(Solution().zeroFilledSubarray(nums))
# @lc code=end