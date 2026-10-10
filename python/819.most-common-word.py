#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        for symbol in "!?',;.": # remove symbols
            paragraph = paragraph.replace(symbol, " ")

        para = paragraph.lower().split()
        banned = set(banned) # checks becomes O(1) in sets
        cnt = {}

        # count words
        for w in para:
            cnt[w] = cnt.get(w, 0) + 1

        # drop banned words
        for w in banned:
            cnt[w] = 0

        # return most common word
        return max(cnt, key=cnt.get)
# @lc code=end

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"] # "ball"

print(Solution().mostCommonWord(paragraph, banned))
