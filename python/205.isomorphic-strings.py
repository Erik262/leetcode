#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}

        for cs, ct in zip(s, t):
            if cs in s2t and s2t[cs] != ct:
                return False
            
            if ct in t2s and t2s[ct] != cs:
                return False
            
            s2t[cs] = ct
            t2s[ct] = cs

        return True
            

    

s = "egg"
t = "add" # True

# s = "foo"
# t = "bar" # False

s = "badc"
t = "baba" # False

print(Solution().isIsomorphic(s, t))
# @lc code=end

