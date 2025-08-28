#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            n &= n - 1
            count += 1

        return count

n = 0b00000000000000000000000000010111 # 4
n = 0b01111111111111111111111111111101 # 30

print(Solution().hammingWeight(n))

        
# @lc code=end

