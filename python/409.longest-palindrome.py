#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
from typing import Counter
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        res = 0
        has_odd = False

        for v in cnt.values():
            if v & 1:
                res += v - 1
                has_odd = True
            else:
                res += v

        return res + 1 if has_odd else res
        
# @lc code=end

