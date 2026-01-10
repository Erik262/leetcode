#
# @lc app=leetcode id=3151 lang=python3
#
# [3151] Special Array I
#
from typing import List
# @lc code=start
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for i in range(1, len(nums)):
            a = nums[i-1]
            b = nums[i]

            if not ((a+b) % 2):
                return False

        return True


nums = [4,3,1,6] # False
nums = [1] # True
nums = [1,5] # False

print(Solution().isArraySpecial(nums))
# @lc code=end

