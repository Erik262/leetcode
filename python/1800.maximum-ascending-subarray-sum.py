#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        inc = best = nums[0]

        for i in range(1, len(nums)):
            a = nums[i-1]
            b = nums[i]

            if a < b:
                if inc == 0:
                    inc += (a+b)
                else:
                    inc += b

            else:
                inc = 0

            best = max(inc, best)

        return best
        
# @lc code=end

