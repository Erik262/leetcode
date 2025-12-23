#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix = {0: 1}

        for n in nums:
            curSum += n
            diff = curSum -  k

            res += prefix.get(diff, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return res
        
# @lc code=end

