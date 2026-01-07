#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
from typing import List
# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = nums[:i]
            right = nums[i+1:]

            if sum(left) == sum(right):
                return i

        return -1

nums = [1,7,3,6,5,6] # 3
nums = [2,1,-1] # 0
print(Solution().pivotIndex(nums))
        
# @lc code=end

