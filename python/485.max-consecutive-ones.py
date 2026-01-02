#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        max_res = 0

        for i in nums:
            if i:
                res += 1
                max_res = max(max_res, res)
            else:
                res = 0

        return max_res
        
# @lc code=end

