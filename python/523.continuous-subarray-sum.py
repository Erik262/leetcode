#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
from typing import List
# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem = 0
        hmap = {0: -1}

        for i, num in enumerate(nums):
            rem = (rem + num) % k

            if rem in hmap:
                if i - hmap[rem] >= 2:
                    return True
            else:
                hmap[rem] = i

        return False


# @lc code=end

