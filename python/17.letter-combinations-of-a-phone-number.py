from typing import List
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # buttons = [hmap[n] for n in digits]

        def dfs(idx, s):
            if len(s) == len(digits):
                res.append(s)
                return
            
            for c in hmap[digits[idx]]:
                dfs(idx + 1, s + c)

        if digits:
            dfs(0, "")
        
        return res
    
    
digits = "34" # ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
# digits = "23" # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# digits = "" # []
# digits = "2" # ["a","b","c"]

print(Solution().letterCombinations(digits))
        
# @lc code=end

