#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        prev = [1]

        for _ in range(1, numRows):
            mid = [prev[j - 1] + prev[j] for j in range(1, len(prev))]
            curr = [1] + mid + [1]
            res.append(curr)
            prev = curr
        
        return res

numRows = 5 # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print(Solution().generate(numRows))
# @lc code=end