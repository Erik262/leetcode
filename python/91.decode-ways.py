#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {len(s): 1}

        for i in range(len(s) - 1, -1, -1): # reverse
            if s[i] == "0":
                hmap[i] = 0
            else:
                hmap[i] = hmap[i+1]


            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                hmap[i] += hmap[i+2]

        return hmap[0]


s = "226" #3
# s = "12" # 2
# s = "01" # 0


print(Solution().numDecodings(s))
        
# @lc code=end

