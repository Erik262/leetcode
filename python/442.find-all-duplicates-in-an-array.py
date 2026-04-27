#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
from typing import List
# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            idx = abs(num) - 1
            n = nums[idx]

            if n < 0:
                res.append(abs(num))
            else:
                nums[idx] = -n

        return res
# @lc code=end

