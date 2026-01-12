#
# @lc app=leetcode id=2264 lang=python3
#
# [2264] Largest 3-Same-Digit Number in String
#

# @lc code=start
class Solution:
    def largestGoodInteger(self, num: str) -> str:

        best = -1
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                best = max(best, int(num[i]))

        return str(best) * 3 if best != -1 else ""
# @lc code=end

