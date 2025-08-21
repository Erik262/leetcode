from typing import List
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        result = []

        while len(result) != (m * n):
            
            # left --> right
            for lr in range(left, right + 1):
                result.append(matrix[top][lr])
            top += 1

            # top --> bottom
            for tb in range(top, bottom + 1):
                result.append(matrix[tb][right])
            right -= 1

            # right --> left
            if top <= bottom:
                for rl in range(right, left - 1, -1):
                    result.append(matrix[bottom][rl])
                bottom -= 1

            # bottom --> top
            if left <= right:
                for bu in range(bottom, top - 1, -1):
                    result.append(matrix[bu][left])
                left += 1

        return result

matrix = [[1,2],[3,4]] # [1,2,4,3]
matrix = [[1,2,3],[4,5,6],[7,8,9]] # [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # [1,2,3,4,8,12,11,10,9,5,6,7]

print(Solution().spiralOrder(matrix))
        
# @lc code=end

