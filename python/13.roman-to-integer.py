#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        amount = 0
        hmap = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            "0": 0
        }

        prev = hmap["0"]
        for c in s:
            diff = 0
            val = hmap[c]
            if prev < val:
                diff = val - 2 * prev
                amount += diff
            else:
                amount += val
            prev = hmap[c]
            
        return amount
                




s = "III" # 3
s = "LVIII" # 58
s = "MCMXCIV" # 1994

print(Solution().romanToInt(s))
        
# @lc code=end

