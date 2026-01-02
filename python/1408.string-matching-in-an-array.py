#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#
from typing import List, Deque, DefaultDict
# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        res = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res

words = ["mass","as","hero","superhero"]
# words = ["leetcoder","leetcode","od","hamlet","am"]
# words = ["blue","green","bu"] # []

print(Solution().stringMatching(words))
        
# @lc code=end

