#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        l, r = 0, len(num) - 1

        while l < r:
            if num[l] == num[r]:
                l += 1
                r -= 1
                continue
            else:
                return False
            
        return True

x = 121 # True
x = -121 # False
x = 10 # False

print(Solution().isPalindrome(x))
        
# @lc code=end

