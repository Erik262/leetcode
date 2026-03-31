#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        cnt = 1

        for ch in s:

            if ch in seen:
                cnt += 1
                seen.clear()

            seen.add(ch)

        return cnt

            


s = "abacaba" # 4
# s = "ssssss" # 6

print(Solution().partitionString(s))
        
        
# @lc code=end

