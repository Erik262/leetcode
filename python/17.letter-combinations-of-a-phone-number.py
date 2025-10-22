from typing import List
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        def dfs(idx: int, prefix: List[str]):
            if idx == len(digits):
                result.append(prefix)
                return

            for c in keypad[digits[idx]]:
                dfs(idx + 1, prefix + c)

        dfs(0, "")
        return result
    
    
digits = "34" # ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# digits = "23" # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# digits = "" # []
# digits = "2" # ["a","b","c"]

print(Solution().letterCombinations(digits))
        
# @lc code=end

