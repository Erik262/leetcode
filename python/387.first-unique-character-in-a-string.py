#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        for i, ch in enumerate(s):
            if freq[ord(ch) - ord('a')] == 1:
                return i

        return -1
# @lc code=end

