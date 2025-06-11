from typing import List
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])
        visited = set()
        print(board)

        def dfs(i: int, j:int, visited: set):

            if i < 0 or i >= rows or j < 0 or j >= cols:
                 return
            
            if board[i][j] == "X" or (i,j) in visited:
                return
            
            visited.add((i,j))
    
            dfs(i + 1, j, visited)
            dfs(i - 1, j, visited)
            dfs(i, j + 1, visited)
            dfs(i, j - 1, visited)            

        for row in range(rows):
            for col in range(cols):
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        dfs(row, col, visited)

        for row in range(rows):
             for col in range(cols):
                  if board[row][col] == "O" and (row, col) not in visited:
                       board[row][col] = "X"




board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

# Output: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","O"]
# ]

print(Solution().solve(board))
        
# @lc code=end

