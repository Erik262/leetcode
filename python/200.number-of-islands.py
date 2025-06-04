from typing import List
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        counter = 0

        def dfs(i: int, j: int):
            
            if (i<0 or 
                i>= rows or 
                j <0 or 
                j>= cols or 
                (i,j) in visited or
                grid[i][j] == '0'):
                return

            visited.add((i,j))

            dfs(i+1, j) # down
            dfs(i, j+1) # right
            dfs(i-1, j) # up
            dfs(i, j-1)

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == '1':
                    dfs(row, col)
                    counter += 1

        return counter



grid = [ # 1
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid = [ # 4
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

# grid = [ # 1
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]


print(Solution().numIslands(grid))

# @lc code=end

