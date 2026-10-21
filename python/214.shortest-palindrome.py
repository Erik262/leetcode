#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        combo = s + '#' + rev
        pref = [0] * len(combo)

        for i in range(1, len(combo)):
            j = pref[i-1]

            while j and combo[i] != combo[j]: 
                j = pref[j-1]

            if combo[i] == combo[j]: 
                j += 1

            pref[i] = j

        return rev[:len(s)-pref[-1]] + s
# @lc code=end

