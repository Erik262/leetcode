#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#
from collections import deque
# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = deque(word1), deque(word2)
        parts = []

        while w1 or w2:
            if w1:
                parts.append(w1.popleft())

            if w2:
                parts.append(w2.popleft())

        return "".join(parts)
# @lc code=end

