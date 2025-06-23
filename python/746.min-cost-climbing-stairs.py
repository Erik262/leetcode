from typing import List
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = [-1] * len(cost) # saves costs!

        def dfs(pos: int):
            if pos >= len(cost):
                return 0
            
            if memory[pos] != -1:
                return memory[pos]
            
            memory[pos] = cost[pos] + min(dfs(pos + 1), dfs(pos + 2))
            return memory[pos]
        
        return min(dfs(0), dfs(1))

# cost = [10,15,20] # 15
cost = [1,100,1,1,1,100,1,1,100,1] # 6

print(Solution().minCostClimbingStairs(cost))

# @lc code=end

