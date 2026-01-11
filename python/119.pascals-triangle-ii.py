#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
from typing import List
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        prev = [1]

        for _ in range(1, rowIndex + 1):
            mid = [prev[j - 1] + prev[j] for j in range(1, len(prev))]
            curr = [1] + mid + [1]
            res.append(curr)
            prev = curr
        
        return res[-1]
    

print(Solution().getRow(1))
# @lc code=end

