class Solution(object):
    def maxProfit(self, prices):
        l_idx = 0
        r_idx = l_idx + 1
        profit = 0

        while r_idx < len(prices):
            if prices[l_idx] < prices[r_idx]:
                profit = max(profit, prices[r_idx] - prices[l_idx])
                r_idx += 1
            else:
                l_idx = r_idx
                r_idx = l_idx + 1

        return profit

prices = [7,1,5,3,6,4] # 5
# prices = [7,6,4,3,1] # 0
# prices = [10,1,5,6,7,1] # 6
# prices = [10,8,7,5,2] # 0
# prices = [1, 2, 3, 4, 5] # 4
# prices = [7]
print(Solution().maxProfit(prices))