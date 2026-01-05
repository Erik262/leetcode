#
# @lc app=leetcode id=3442 lang=python3
#
# [3442] Maximum Difference Between Even and Odd Frequency I
#
from typing import Counter
# @lc code=start
class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd_max, even_min = 0, len(s) 

        for ct in cnt.values():
            if ct % 2:
                odd_max = max(odd_max, ct)
            else:
                even_min = min(even_min, ct)

        return odd_max - even_min

s = "aaaaabbc" # 3
s = "abcabcab" # 1
s = "tzt" # -1
s = "aabbbbccc" # 1


print(Solution().maxDifference(s))
# @lc code=end

