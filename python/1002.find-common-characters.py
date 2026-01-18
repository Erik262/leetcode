#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#
from typing import List
# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])

        res = []
        word1 = set(words[0])

        for ch in word1:
            freq = min([word.count(ch) for word in words])
            res += [ch] * freq

        return res
# @lc code=end

