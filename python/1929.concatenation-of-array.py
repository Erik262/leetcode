#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n

        for i in range(n):
            ans[i] = ans[i+n] = nums[i]

        return ans

        
# @lc code=end

