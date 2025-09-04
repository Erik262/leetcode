#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i: int):
            if i >= n:
                return i == n

            if cache[i] != -1:
                return cache[i]

            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]

        return dfs(0)


n = 2 # 2
n = 3 # 3
n = 5 # 5

print(Solution().climbStairs(n))
        
# @lc code=end

