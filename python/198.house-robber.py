from typing import List
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        memory = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if memory[i] != -1:
                return memory[i]
            
            memory[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))

            return memory[i]
        
        return dfs(0)


nums = [1,1,3,3] # 4
nums = [2,9,8,3,6] # 16
nums=[5,1,2,10,6,2,7,9,3,1] # 27

print(Solution().rob(nums))

# @lc code=end

