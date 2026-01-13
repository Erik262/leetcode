#
# @lc app=leetcode id=2490 lang=python3
#
# [2490] Circular Sentence
#

# @lc code=start
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False

        for i in range(len(sentence) - 2):
            if sentence[i+1] != " ":
                continue

            if sentence[i] != sentence[i+2]:
                return False

        return True
# @lc code=end

