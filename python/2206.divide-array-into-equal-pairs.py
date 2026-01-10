#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#
from typing import List, Counter
# @lc code=start
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        
        for k, v in cnt.items():
            if v & 1:
                return False

        return True
# @lc code=end

