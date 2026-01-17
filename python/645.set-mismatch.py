#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
from typing import List
# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = 0, 0
        hmap = {}
        n = len(nums)
        
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for i in range(1, n+1):
            if hmap.get(i, 0) == 0:
                missing = i
            elif hmap[i] == 2:
                dup = i

        return [dup, missing]
# @lc code=end

