#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*' and dp[0][j - 2]:
                dp[0][j] = True

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] != '*':
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]

        return dp[len(s)][len(p)]

s = "aa" # False
p = ".b"

s = "nnn" # True
p = "n*"

# s = "xyz" # True
# p = ".*z"

print(Solution().isMatch(s, p))
        
# @lc code=end

