#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

        return result



s = "abc" # 3
s = "aaa" # 6

print(Solution().countSubstrings(s))
        
# @lc code=end

