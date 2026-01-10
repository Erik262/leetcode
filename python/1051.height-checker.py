#
# @lc app=leetcode id=1051 lang=python3
#
# [1051] Height Checker
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0

        for a, b in zip(heights, sorted(heights)):
            if a != b:
                res += 1

        return res
# @lc code=end

