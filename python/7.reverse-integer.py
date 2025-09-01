#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = - 2**31
        INT_MAX = 2**31 - 1
        result = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x:
            digit = int(x % 10) 
            x = int(x / 10)

            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            if result < INT_MIN // 10 or (result == INT_MIN // 10 and digit < INT_MIN % 10):
                return 0
            result = (result * 10) + digit

        return result * sign


x = 1234 # 4321
x = -1234 # -4321
# x = 1234236467 # 0

print(Solution().reverse(x))
        
# @lc code=end

