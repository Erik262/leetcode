from typing import List
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def is_pali(l: int, r: int):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i: int, j: int):
            if j >= len(s):
                if i == j:
                    result.append(part.copy())
                return

            if is_pali(i, j):
                part.append(s[i:j+1])
                dfs(j+1, j+1)
                part.pop()

            dfs(i, j+1)

        dfs(0,0)

        return result


s = "aab" # [["a","a","b"],["aa","b"]]
# s = "a" # [["a"]]

print(Solution().partition(s))
        
# @lc code=end