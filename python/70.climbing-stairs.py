#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one


n = 2 # 2
n = 3 # 3
n = 5 # 5

print(Solution().climbStairs(n))
        
# @lc code=end

