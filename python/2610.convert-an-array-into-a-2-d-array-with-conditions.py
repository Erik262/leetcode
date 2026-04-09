#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#
from typing import List
# @lc code=start
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        result = []

        for x in nums:
            if freq[x] == len(result):
                result.append([])
            result[freq[x]].append(x)
            freq[x] += 1

        return result 
# @lc code=end

