#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            j = 0

            while j < m:
                if haystack[i+j] != needle[j]:
                    break
                j += 1

            if j == m:
                return i

        return -1
        
# @lc code=end

