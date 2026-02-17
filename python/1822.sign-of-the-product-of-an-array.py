#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#
from typing import List
# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 1

        for num in nums:
            if num < 0:
                neg *= -1

            if num == 0:
                return 0

        return neg  
    

nums = [-1,-2,-3,-4,3,2,1]
print(Solution().arraySign(nums))
# @lc code=end

