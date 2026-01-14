#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
class Solution:
    def minOperations(self, s: str) -> int:
        cnt = 0

        for i, ch in enumerate(s):
            curr = '0' if i % 2 == 0 else '1'

            if ch != curr:
                cnt += 1

        return min(cnt, len(s) - cnt)
        
# @lc code=end

