#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
from typing import List
from functools import cmp_to_key
# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        
        def cmp(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
            
        strs = sorted(strs, key=cmp_to_key(cmp))

        return str(int("".join(strs)))

nums = [3,30,34,5,9] # "9534330"
print(Solution().largestNumber(nums))

        
# @lc code=end

