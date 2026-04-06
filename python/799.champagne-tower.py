#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0] * (r + 1) for r in range(query_row + 1)]
        dp[0][0] = float(poured)

        for r in range(query_row):
            for c in range(r + 1):
                overflow = max(0.0, dp[r][c] - 1.0) / 2.0

                if overflow > 0:
                    dp[r+1][c] += overflow
                    dp[r+1][c+1] += overflow

        return min(1.0, dp[query_row][query_glass])

poured = 2
query_row = 1
query_glass = 1 # 0.5

print(Solution().champagneTower(poured, query_row, query_glass))
# @lc code=end

