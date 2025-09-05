from typing import List
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def dfs(i: int):
            if i >= len(cost):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            
            return cache[i]

        return min(dfs(0), dfs(1))

# cost = [10,15,20] # 15
cost = [1,100,1,1,1,100,1,1,100,1] # 6

print(Solution().minCostClimbingStairs(cost))

# @lc code=end

