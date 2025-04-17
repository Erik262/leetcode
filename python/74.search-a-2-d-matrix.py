#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r:
            m = (l + r) // 2
            n = matrix[m // cols][m % cols]

            if target > n:
                l = m + 1
            elif target < n:
                r = m - 1
            else:
                return True
                
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] # True
target = 3
        
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] #  False
# target = 13

print(Solution().searchMatrix(matrix, target))

# @lc code=end

