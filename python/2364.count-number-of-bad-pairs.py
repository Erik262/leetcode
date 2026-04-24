#
# @lc app=leetcode id=2364 lang=python3
#
# [2364] Count Number of Bad Pairs
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        good = 0

        for i, num in enumerate(nums):
            key = i - num
            good += count[key]
            count[key] += 1

        n = len(nums)
        total = n * (n-1) // 2

        return total - good

                
nums = [4,1,3,3] # 5
print(Solution().countBadPairs(nums))
# @lc code=end

