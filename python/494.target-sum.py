from typing import List
from collections import defaultdict
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for i in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count           
                dp[i + 1][total - nums[i]] += count           

        return dp[len(nums)][target]


nums = [2,2,2] # 3
target = 2

# nums = [1,1,1,1,1] # 5
# target = 3

# nums = [1] # 1
# target = 1

print(Solution().findTargetSumWays(nums, target))
        
# @lc code=end

