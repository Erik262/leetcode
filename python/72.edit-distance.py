#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1, w2 = len(word1), len(word2)

        if w1 < w2: # we want to loop over the largest one w1
            w1, w2 = w2, w1
            word1, word2 = word2, word1

        dp = [w2 - i for i in range(w2 + 1)]

        for i in range(w1 - 1, -1, -1):
            dp_next = dp[w2]
            dp[w2] = w1 - i
            for j in range(w2 - 1, -1, -1):
                temp = dp[j]
                if word1[i] == word2[j]:
                    dp[j] = dp_next
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], dp_next)
                dp_next = temp

        return dp[0]



word1 = "monkeys" # 2
word2 = "money"

# word1 = "neatcdee" # 3
# word2 = "neetcode"

print(Solution().minDistance(word1, word2))
        
# @lc code=end

