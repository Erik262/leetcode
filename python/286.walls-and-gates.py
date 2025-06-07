from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def dfs(i: int, j: int, dist: int):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1 or grid[i][j] < dist:
                return 0
            
            if grid[i][j] > dist:
                grid[i][j] = dist
            
            return dfs(i-1,j, dist+1) + dfs(i,j-1, dist+1) + dfs(i+1,j, dist+1) + dfs(i,j+1, dist+1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:

                    grid[row][col] = min(grid[row][col], dfs(row,col, 0))





# INF = 2147483647
grid = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]

# grid = [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]

print(Solution().islandsAndTreasure(grid))