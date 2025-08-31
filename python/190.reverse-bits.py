#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = n & 1
            result = (result << 1 ) | bit
            n >>= 1

        return result
        
n = 0b00000000000000000000000000010101 # 21
#  (10101000000000000000000000000000) 2818572288

print(Solution().reverseBits(n))

        
# @lc code=end

