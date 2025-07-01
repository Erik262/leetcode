from typing import List
from collections import deque
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if s[i: i + len(word)] == word and (i + len(word)) <= len(s):
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    break

        return dp[0]


        



s = "neetcode"
wordDict = ["neet","code"] # True

s = "applepenapple"
wordDict = ["apple","pen","ape"] # True

# s = "catsincars"
# wordDict = ["cats","cat","sin","in","car"] # False

print(Solution().wordBreak(s, wordDict))
        
# @lc code=end

