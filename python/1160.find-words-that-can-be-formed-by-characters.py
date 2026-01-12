#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
from typing import List, Counter
# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        base = [0] * 26
        res = 0

        for ch in chars:
            base[ord(ch) - 97] += 1


        for w in words:
            need = [0] * 26
            ok = True
            
            for ch in w:
                i = ord(ch) - 97
                need[i] += 1

                if need[i] > base[i]:
                    ok = False
                    break
            if ok:
                res += len(w)

        return res


words = ["cat","bt","hat","tree"]
chars = "atach" # 6

print(Solution().countCharacters(words, chars))
        
# @lc code=end

