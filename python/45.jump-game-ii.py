from typing import List
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)

            if i == end:
                jumps += 1
                end = farthest

        return jumps

nums = [2,4,1,1,1,1] # 2
nums = [2,1,2,1,0] # 2


print(Solution().jump(nums))
        
# @lc code=end

