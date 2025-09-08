from typing import List
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(rem: int):
            if rem == 0:
                return 0
            
            if rem < 0:
                return float('inf')

            if rem in memo:
                return memo[rem]

            best = float('inf')
            for c in coins:
                sub = dfs(rem - c)

                if sub != float('inf'):
                    best = min(best, sub + 1)
            
            memo[rem] = best
            return best

        result = dfs(amount)
        return -1 if result == float('inf') else result
        

coins = [1,5,10] # 3
amount = 12

# coins = [2] # -1
# amount = 3

# coins = [1] # 0
# amount = 0

print(Solution().coinChange(coins, amount))

# @lc code=end

