#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#
from typing import List
# @lc code=start
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hmap = {}

        for n in nums:
            num = ""

            for d in str(n):
                digit = int(d)
                num += str(mapping[digit])
                
            hmap[n] = int(num)

        res = sorted(nums, key=hmap.get)

        return res 
# @lc code=end

