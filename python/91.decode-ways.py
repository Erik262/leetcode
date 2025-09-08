#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * (len(s) + 1)

        def dfs(i: int):
            if i >= len(s):
                return 1
            
            if s[i] == '0':
                return 0

            if memo[i] != -1:
                return memo[i]

            # one step
            ways = dfs(i + 1)
            
            # two steps
            if i + 1 < len(s) and '10' <= s[i:i+2] <= '26':
                ways += dfs(i + 2)

            memo[i] = ways
            return ways

        return dfs(0)


s = "226" #3
# s = "12" # 2
# s = "01" # 0


print(Solution().numDecodings(s))
        
# @lc code=end

