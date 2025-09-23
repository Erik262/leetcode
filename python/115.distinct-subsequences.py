#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = {}

        def dfs(i: int, j: int):
            if n - i < m - j:
                return 0

            if j >= m:
                return 1

            if i >= n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i, j)]

        return dfs(0, 0)
            
s = "caaat" # 3
t = "cat"

s = "xxyxy" # 5
t = "xy"

print(Solution().numDistinct(s, t))
        
# @lc code=end

