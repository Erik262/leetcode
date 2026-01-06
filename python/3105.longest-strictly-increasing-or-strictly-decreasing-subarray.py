#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec, best = 1, 1, 1

        for i in range(1, len(nums)):
            a = nums[i-1]
            b = nums[i]

            if a < b:
                inc += 1
                dec = 1

            elif a > b:
                dec += 1
                inc = 1

            else:
                inc = dec = 1

            best = max(inc, dec, best)

        return best
        
# @lc code=end

