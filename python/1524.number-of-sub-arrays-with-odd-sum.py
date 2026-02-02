#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1_000_000_007

        even = 1
        odd = 0
        res = 0

        prefix_sum = 0
        for x in arr:
            prefix_sum += x

            if prefix_sum % 2 == 1:
                odd += 1
                res += even
            else:
                even += 1
                res += odd

        return res % MOD
# @lc code=end

