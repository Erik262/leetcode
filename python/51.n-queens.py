from typing import List
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        col = set()
        positive = set()
        negative = set()

        def dfs(row):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (row + c) in positive or (row - c) in negative:
                    continue
                
                col.add(c)
                positive.add(row + c)
                negative.add(row - c)
                board[row][c] = "Q"

                dfs(row + 1)

                col.remove(c)
                positive.remove(row + c)
                negative.remove(row - c)
                board[row][c] = "."

        dfs(0)
        return res


n = 4 # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

print(Solution().solveNQueens(n))
# n = 1 # [["Q"]]
# @lc code=end