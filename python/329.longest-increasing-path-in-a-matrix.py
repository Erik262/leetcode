from typing import List
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = {}

        def dfs(row, col, preVal):
            if (row < 0 or row == rows or 
                col < 0 or col == cols or 
                matrix[row][col] <= preVal):
                return 0
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            result = 1
            result = max(result, 1 + dfs(row + 1, col, matrix[row][col])) # down
            result = max(result, 1 + dfs(row - 1, col, matrix[row][col])) # up
            result = max(result, 1 + dfs(row, col + 1, matrix[row][col])) # right
            result = max(result, 1 + dfs(row, col - 1, matrix[row][col])) # left
            dp[(row, col)] = result

            return result
        
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, -1)

        return max(dp.values())


matrix = [[5,5,3],[2,3,6],[1,1,1]] # 4
matrix = [[1,2,3],[2,1,4],[7,6,5]] # 7

print(Solution().longestIncreasingPath(matrix))
        
# @lc code=end

