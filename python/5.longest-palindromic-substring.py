#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = ""

        def expand(s: str, l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l+1:r]

        for i in range(len(s)):
            p1 = expand(s,i, i)
            p2 = expand(s, i, i+1)

            longest = p1 if len(p1) > len(p2) else p2
            max_pali = longest if len(longest) > len(max_pali) else max_pali
        
        return max_pali
                 


s = "babad" # "bab"
# s = "cbbd" # "bb"

print(Solution().longestPalindrome(s))

        
# @lc code=end

