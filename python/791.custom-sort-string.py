#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = [0] * 26
        result = []

        for ch in s:
            freq[ord(ch) - 97] += 1
        
        for ch in order:
            i = ord(ch) - 97

            if freq[i]:
                result.append(ch * freq[i])
                freq[i] = 0

        for i in range(26):
            if freq[i]:
                result.append(chr(i + 97) * freq[i])

        return "".join(result)


order = "cba"
s = "abcd" # "cbad"


order = "bcafg"
s = "abcd" # "bcad"

order = "bfg"
s = "agbfcdb" # "bbfgacd"


print(Solution().customSortString(order, s))
# @lc code=end

