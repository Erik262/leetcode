#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False

        memo = {}
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True

            if (i,j) in memo:
                return memo[(i, j)]
                
            k = i + j
            take1 = (i < len(s1) and s1[i] == s3[k] and dfs(i+1, j))
            take2 = (j < len(s2) and s2[j] == s3[k] and dfs(i, j+1))

            take = take1 or take2
            memo[(i, j)] = take

            return memo[(i, j)]

        return dfs(0, 0)



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

