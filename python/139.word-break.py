from typing import List
from collections import deque
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(i: int) -> bool:
            if i in memo:
                return memo[i]

            if i == n:
                return True

            for j in range(i + 1, n + 1):
                if s[i:j] in words and dfs(j):
                    
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)

s = "neetcode"
wordDict = ["neet","code"] # True

s = "applepenapple"
wordDict = ["apple","pen","ape"] # True

# s = "catsincars"
# wordDict = ["cats","cat","sin","in","car"] # False

print(Solution().wordBreak(s, wordDict))
        
# @lc code=end

