#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def is_pali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1
            
            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return (
                    is_pali(l + 1, r) or is_pali(l, r -1)
                    )
        
        return True        
# @lc code=end

