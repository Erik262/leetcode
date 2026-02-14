#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
from typing import List
# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                if changed:
                    return False

                changed = True

                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]

        return True
        

nums = [3,4,2,3] # False
print(Solution().checkPossibility(nums))




# @lc code=end

