#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i:int, holding: bool) -> int:
            if i >= len(prices):
                return 0

            if (i, holding) in dp:
                return dp[(i, holding)]

            # skip
            res = dfs(i+1, holding)

            if holding == 1:
                # sell
                res = max(res, prices[i] + dfs(i+1, 0))
            else:
                # buy
                res = max(res, -prices[i] + dfs(i+1, 1))

            dp[(i, holding)] = res
            return res

        return dfs(0,0)
        
# @lc code=end

