from typing import List
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0]) # rows, cols
        row_zero = any(matrix[0][j] == 0 for j in range(n))
        col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row_zero:
            for i in range(n):
                matrix[0][i] = 0
        
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0


matrix = [[0,1],[1,0]]  # [[0,0],[0,0]]
matrix = [[1,2,3],[4,0,5],[6,7,8]] # [[1,0,3],[0,0,0],[6,0,8]]

print(Solution().setZeroes(matrix))

# @lc code=end

