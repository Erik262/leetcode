#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        seen = [False] * (n + 1)

        for x in nums:
            if 1 <= x <= n:
                seen[x] = True

        for i in range(1, n+1):
            if not seen[i]:
                return i

        return n+1 
# @lc code=end

