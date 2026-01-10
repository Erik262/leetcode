#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
from typing import List
# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = False
        dec = False

        for i in range(1, len(nums)):
            a = nums[i-1]
            b = nums[i]

            if a < b:
                inc = True
            
            elif a > b:
                dec = True

            if inc and dec:
                return False

        return True

# @lc code=end

