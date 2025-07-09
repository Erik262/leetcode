#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s2) + len(s1):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True

                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]



s1 = "aaaa" # True
s2 = "bbbb"
s3 = "aabbbbaa"

# s1 = "" # True
# s2 = ""
# s3 = ""

# s1 = "abc" # False
# s2 = "xyz"
# s3 = "abxzcy"

s1="aabcc" # True
s2="dbbca"
s3="aadbbcbcac"

print(Solution().isInterleave(s1, s2, s3))
        
# @lc code=end

