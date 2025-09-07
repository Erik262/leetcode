#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = ""

        def expand(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return s[l+1:r]

        for i in range(len(s)):
            l1 = expand(s, i, i) # odd
            l2 = expand(s, i, i + 1) # even

            longest = l1 if len(l1) > len(l2) else l2

            if len(longest) > len(max_pali):
                max_pali = longest

        return max_pali
                 


s = "babad" # "bab"
# s = "cbbd" # "bb"

print(Solution().longestPalindrome(s))

        
# @lc code=end

