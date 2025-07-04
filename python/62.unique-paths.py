#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)] # with 'gaps'
        dp[m - 1][n - 1] = 1 # setting our goal position

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i][j] + dp[i + 1][j] + dp[i][j + 1]
                
        return dp[0][0]


# m = 3 # 21
# n = 6

m = 3 # 6
n = 3

print(Solution().uniquePaths(m, n))  
# @lc code=end

