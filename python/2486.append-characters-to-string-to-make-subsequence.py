#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l_idx, r_idx = 0, 0

        while l_idx < len(s) and r_idx < len(t):
            if s[l_idx] == t[r_idx]:
                r_idx += 1
            l_idx += 1
        
        return len(t) - r_idx
    
s = "lbg"
t = "g" # 0
print(Solution().appendCharacters(s, t))
        
# @lc code=end

