#
# @lc app=leetcode id=2418 lang=python3
#
# [2418] Sort the People
#
from typing import List
# @lc code=start
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = sorted(zip(heights, names), reverse=True)
        return [y for x, y in res]
# @lc code=end

