from typing import List
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(part.copy())
                return
            
            if self.pali(s, j, i):
                part.append(s[j:i+1])
                dfs(i+1, i+1)
                part.pop()
            
            dfs(j, i+1)

        dfs(0,0)
        return res

    def pali(self, s, l , r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


s = "aab" # [["a","a","b"],["aa","b"]]
# s = "a" # [["a"]]

print(Solution().partition(s))
        
# @lc code=end