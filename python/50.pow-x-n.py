#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        def _pow(x, k):
            if k == 0:
                return 1.0
            
            half = _pow(x, k // 2)
            
            if k % 2 == 0:
                return half * half
            else:
                return half * half * x
            
        return _pow(x, n)

        

x = 2.00000 # 32.00000
n = 5

# x = 1.10000 # 2.59374
# n = 10

# x = 2.00000 # 0.12500
# n = -3

print(Solution().myPow(x, n))

# @lc code=end

