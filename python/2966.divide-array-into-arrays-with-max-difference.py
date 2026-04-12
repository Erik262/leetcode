#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#
from typing import List
# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums), 3):
            group = nums[i:i+3]

            if group[2] - group[0] > k:
                return []
            
            res.append(group)

        return res 
# @lc code=end

