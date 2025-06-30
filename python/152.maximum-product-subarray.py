from typing import List
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)

            result = max(curMax, result)

        return result

nums = [1,2,-3,4] # 4
nums = [-2,-1] # 2
nums = [2,3,-2,4] # 6

print(Solution().maxProduct(nums))
        
# @lc code=end

