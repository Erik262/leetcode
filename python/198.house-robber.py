from typing import List
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0, 0

        for house in nums:
            tmp = max(r1 + house, r2)
            r1 = r2
            r2 = tmp

        return r2


nums = [1,1,3,3] # 4
nums = [2,9,8,3,6] # 16
nums=[5,1,2,10,6,2,7,9,3,1] # 27

print(Solution().rob(nums))

# @lc code=end

