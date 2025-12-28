#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l_idx, r_idx = 0, 0

        while l_idx < len(s) and r_idx < len(t):
            if s[l_idx] == t[r_idx]:
                l_idx += 1

            r_idx += 1

        return l_idx == len(s)
        
# @lc code=end

