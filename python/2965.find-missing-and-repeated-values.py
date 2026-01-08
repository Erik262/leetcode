#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#
from typing import List, Counter
# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = [num for row in grid for num in row]

        freq = Counter(nums)
        repeated = -1
        missing = -1

        for val in range(1, n*n + 1):
            if freq[val] == 2:
                repeated = val
            elif freq[val] == 0:
                missing = val


        return [repeated, missing]

# @lc code=end

