#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#
from typing import List
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        ans = -1

        for x in nums:
            total += x
            
            if total - x > x:
                ans = total

        return ans
# @lc code=end