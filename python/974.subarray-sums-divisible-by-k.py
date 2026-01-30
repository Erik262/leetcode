#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
from typing import List
# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        
        res = 0
        prefix = 0
        for num in nums:
            prefix += num
            reminder = prefix % k

            res += cnt[reminder]
            cnt[reminder] += 1

        return res   
        
# @lc code=end

