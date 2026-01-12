#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#
from typing import List, Counter
# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        cnt_chars = Counter(chars)

        for word in words:
            cnt_word = Counter(word)
            if not (cnt_word - cnt_chars):
                res += len(word)

        return res


words = ["cat","bt","hat","tree"]
chars = "atach" # 6

print(Solution().countCharacters(words, chars))
        
# @lc code=end

