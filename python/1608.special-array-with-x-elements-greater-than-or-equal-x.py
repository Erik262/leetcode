#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#
from typing import List
# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)

        for x in range(n + 1):
            cnt = 0

            for num in nums:
                if num >= x:
                    cnt += 1

            if cnt == x:
                return x

        return -1
# @lc code=end

