#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
#

# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for i in range(1, len(s)):
            a = ord(s[i-1])
            b = ord(s[i])

            res += abs(a - b)

        return res
        
# @lc code=end

