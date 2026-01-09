#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        p2w = {}
        w2p = {}

        for p, w in zip(pattern, words):
            if p in p2w and p2w[p] != w:
                return False
            if w in w2p and w2p[w] != p:
                return False

            p2w[p] = w
            w2p[w] = p

        return True
    
s = "dog cat cat dog" # True
s = "dog dog dog dog" # False
pattern = "abba" 

print(Solution().wordPattern(pattern, s))
# @lc code=end

