#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#
from typing import List
# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drops = 0

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                drops += 1
                if drops > 1:
                    return False
                    
        return True

nums = [3,4,5,1,2] # True
nums = [2,1,3,4] # False        
nums = [1,2,3] # True

print(Solution().check(nums))
        
# @lc code=end

