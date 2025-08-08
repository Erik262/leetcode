from typing import List
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            if i > maxReach: 
                return False
            
            maxReach = max(maxReach, i + nums[i])

            if maxReach >= len(nums) - 1: 
                return True
            

nums = [1,2,0,1,0] # True
nums = [1,2,1,0,1] # False

nums = [2,3,1,1,4] # True

print(Solution().canJump(nums))
# @lc code=end

