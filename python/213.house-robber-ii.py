from typing import List
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i: int, num: List[int], mem: List[int]):
            if i >= len(num):
                return 0
            
            if mem[i] != -1:
                return mem[i]
            
            mem[i] = max(dfs(i + 1, num, mem), num[i] + dfs(i + 2, num, mem))

            return mem[i]
        
        def _dfs(num: List[int]):
            memory = [-1] * len(nums)
            return max(dfs(0, num, memory), dfs(1, num, memory))
        
        if len(nums) == 1:
            return nums[0]

        return max(_dfs(nums[1:]), _dfs(nums[:-1]))



nums = [3,4,3] # 4 ## 6
nums = [2,9,8,3,6] # 15 ## 16
nums = [1,2,3,1] # 4

print(Solution().rob(nums))
        
# @lc code=end

