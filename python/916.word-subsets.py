#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#
from typing import List, Counter

# @lc code=start
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        need_freq = Counter()

        for w2 in words2:
            curr_freq = Counter(w2)

            for ch in curr_freq:
                need_freq[ch] = max(curr_freq[ch], need_freq[ch])


        res = []
        for w1 in words1:
            curr_freq = Counter(w1)

            if all(curr_freq[ch] >= need_freq[ch] for ch in need_freq):
                res.append(w1)

        return res

                

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

print(Solution().wordSubsets(words1, words2))

# @lc code=end
