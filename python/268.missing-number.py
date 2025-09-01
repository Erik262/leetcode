from typing import List
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        t_sum = n * (n + 1) // 2
        n_sum = sum(nums)

        return t_sum - n_sum

nums = [1,2,3] # 0
nums = [0,2] # 1
nums = [3,0,1] # 2
nums = [0,1] # 2
nums = [9,6,4,2,3,5,7,0,1] # 8

print(Solution().missingNumber(nums))
        
# @lc code=end

