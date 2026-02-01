#
# @lc app=leetcode id=1930 lang=python3
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        pali_set = set(s)

        for c in pali_set:
            start = s.find(c)
            end = s.rfind(c)

            if start < end:
                res += len(set(s[start+1:end]))

        return res

s = "adc"
s = "bbcbaba"
print(Solution().countPalindromicSubsequence(s))
# @lc code=end

