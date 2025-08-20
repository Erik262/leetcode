from typing import List
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            matrix[r].reverse()

        return matrix


matrix = [[1,2],[3,4]] # [[3,1],[4,2]]
matrix = [[1,2,3],[4,5,6],[7,8,9]] # [[7,4,1],[8,5,2],[9,6,3]]

print(Solution().rotate(matrix))

        
# @lc code=end

