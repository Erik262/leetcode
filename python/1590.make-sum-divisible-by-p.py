#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#
from typing import List
# @lc code=start
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        last = {0: -1}
        prefix = 0
        ans = len(nums)

        for i, x in enumerate(nums):
            prefix += x
            reminder = prefix % p
            need = (reminder - target) % p

            if need in last:
                ans = min(ans, i - last[need])
            last[reminder] = i

        return ans if ans < len(nums) else -1
# @lc code=end

