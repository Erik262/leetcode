#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sum_sqr(n: int) -> int:
            s = 0

            while n:
                n, d = divmod(n, 10)
                s += d*d

            return s

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum_sqr(n)

        return n == 1


n = 100 # True
# n = 101 # False

print(Solution().isHappy(n))
        
# @lc code=end

