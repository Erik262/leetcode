#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0

        for i in range(len(s) - 1):
            pre = roman[s[i]]
            pos = roman[s[i+1]]

            if pre < pos:
                result -= pre
            else:
                result += pre

        return result + roman[s[-1]]

s = "III" # 3
s = "LVIII" # 58
s = "MCMXCIV" # 1994

print(Solution().romanToInt(s))
        
# @lc code=end

