from typing import List
import math
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hmap = [math.inf] * (amount + 1)
        hmap[0] = 0

        for i in range (1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    hmap[i] = min(hmap[i], 1 + hmap[i - c])
        
        return hmap[amount] if hmap[amount] != math.inf else -1
        

coins = [1,5,10] # 3
amount = 12

# coins = [2] # -1
# amount = 3

# coins = [1] # 0
# amount = 0

print(Solution().coinChange(coins, amount))

# @lc code=end

