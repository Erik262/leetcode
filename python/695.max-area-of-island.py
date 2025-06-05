from typing import List
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i: int, j: int):

            if (i<0 or i>= rows or j<0 or j>= cols or (i,j) in visited or grid[i][j] == 0):
                return 0


            if (i,j) not in visited and grid[i][j] == 1:
                visited.add((i,j))
                return 1 + dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j) + dfs(i,j+1)

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == 1:
                    max_area = max(max_area, dfs(row,col))

        return max_area


grid = [ # 6
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

print(Solution().maxAreaOfIsland(grid))
        
# @lc code=end

