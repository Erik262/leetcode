#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#
from typing import List
# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        base = [0] * 26
        res = 0

        for ch in allowed:
            base[ord(ch) - 97] = 1

        for w in words:
            need = [0] * 26
            ok = True

            for ch in w:
                i = ord(ch) - 97
                need[i] = 1

                if need[i] != base[i]:
                    ok = False
                    break

            if ok:
                res += 1

        return res

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"] # 2

print(Solution().countConsistentStrings(allowed, words))
# @lc code=end

