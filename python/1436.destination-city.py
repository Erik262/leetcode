#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#
from typing import List
# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = set(a for a, b in paths)

        for a, b in paths:
            if b not in out:
                return b


# @lc code=end

