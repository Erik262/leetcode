from typing import List
from collections import defaultdict
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        # prunning
        rem = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            rem[i] = rem[i + 1] + nums[i]

        def dfs(i: int, amount: int):
            if abs(target - amount) > rem[i]:
                return 0

            if i == n:
                if amount == target:
                    return 1
                else:
                    return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            add = dfs(i + 1, amount + nums[i])
            sub = dfs(i + 1, amount - nums[i])

            memo[(i, amount)] = add + sub

            return memo[(i, amount)]

        return dfs(0, 0)


nums = [2,2,2] # 3
target = 2

# nums = [1,1,1,1,1] # 5
# target = 3

# nums = [1] # 1
# target = 1

print(Solution().findTargetSumWays(nums, target))
        
# @lc code=end

