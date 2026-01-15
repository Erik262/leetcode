#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        n = len(s)

        for i in range(n - 1):
            if n - i - 2 <= res:
                break

            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    res = max(res, j - i - 1)
                    break
        return res
        
s = "abca" # 2
s = "aa" # 0
print(Solution().maxLengthBetweenEqualCharacters(s))
# @lc code=end

