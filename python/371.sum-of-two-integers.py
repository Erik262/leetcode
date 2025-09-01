#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask

        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)


a = 1 # 2
b = 1

a = 4 # 11
b = 7

a = 3 # 8
b = 5

print(Solution().getSum(a, b))
        
# @lc code=end