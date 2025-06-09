from typing import List
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_time = 0


        def dfs(i: int, j: int, minute: int):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return
            
            if grid[i][j] == 0:
                return
            
            if grid[i][j] != 1 and grid[i][j] < minute:
                return
            
            grid[i][j] = minute

            dfs(i+1,j,minute+1)
            dfs(i-1,j,minute+1)
            dfs(i,j+1,minute+1)
            dfs(i,j-1,minute+1)

        for row in range(rows):
            for col in range(cols):
                
                if grid[row][col] == 2:
                    dfs(row, col, 2)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
                
                if grid[row][col] > 2:
                    max_time = max(max_time, grid[row][col])

        return max_time - 2 if max_time else 0


grid = [[2,1,1],[1,1,0],[0,1,1]] # 4
# grid = [[2,1,1],[0,1,1],[1,0,1]] # -1
# grid = [[0,2]] # 0

print(Solution().orangesRotting(grid))
        
# @lc code=end

