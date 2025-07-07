from typing import List
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] <= j:
                    dp[j] = dp[j] + dp[j - coins[i]]

        return dp[amount]


amount = 5
coins = [1,2,5] # 4

amount = 3
coins = [2] # 0

amount = 10
coins = [10] # 1

print(Solution().change(amount, coins))
        
# @lc code=end

