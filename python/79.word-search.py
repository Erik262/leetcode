from typing import List
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(i: int, j: int, idx: int) -> bool:

            if idx == len(word):
                return True

            # boundaries
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            
            # when character not matches
            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#' # marking when visited

            found = (
                dfs(i + 1, j, idx + 1) or # down
                dfs(i - 1, j, idx + 1) or # up
                dfs(i, j + 1, idx + 1) or # right
                dfs(i, j - 1, idx + 1)    # left
            )

            board[i][j] = temp
            return found

        for row in range(rows):
            for col in range(cols):

                if dfs(row, col, 0):
                    return True
                
        return False




board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT" # True

# board = [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
# ]
# word = "BAT" # False


print(Solution().exist(board, word))
# @lc code=end