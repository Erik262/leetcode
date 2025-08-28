from typing import List
from collections import Counter
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            result = result ^ n
            
        return result




nums = [3,2,3] # 2
nums = [7,6,6,7,8] # 8

print(Solution().singleNumber(nums))
        
# @lc code=end

