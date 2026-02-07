#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#
from typing import List
# @lc code=start
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        top = grid[0]
        bot = grid[1]

        top_right = sum(top)
        bot_left = 0

        result = float("inf")

        for i in range(n):
            top_right -= top[i]

            result = min(result, max(top_right, bot_left))

            bot_left += bot[i]

        return result
    
grid = [[3,3,1],[8,5,2]]
grid = [[2,5,4],[1,5,1]] # 4

# grid = [[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]] # 63

print(Solution().gridGame(grid))
        
# @lc code=end

