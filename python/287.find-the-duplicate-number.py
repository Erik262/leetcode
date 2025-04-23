from typing import List
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hmap = {}

        for idx, n in enumerate(nums):
            if n not in hmap:
                hmap[n] = idx
            else:
                return n
            

nums = [1,3,4,2,2] # 2
# nums = [3,1,3,4,2] # 3
# nums = [3,3,3,3,3] # 3




print(Solution().findDuplicate(nums))
        
# @lc code=end

