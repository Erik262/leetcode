#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split(' ') + s2.split(' ')
        cnt = Counter(words)

        result = []

        for word, freq in cnt.items():
            if freq == 1:
                result.append(word)

        return result

# @lc code=end

