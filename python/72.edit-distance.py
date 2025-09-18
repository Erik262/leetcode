#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        w1, w2 = len(word1), len(word2)

        def dfs(i: int, j:int):
            # end
            if i == w1:
                return w2 - j
            
            if j == w2:
                return w1 - i

            if (i, j) in memo:
                return memo[(i, j)]

            # edits
            if word1[i] != word2[j]:
                insert = 1 + dfs(i, j + 1)
                delete = 1 + dfs(i + 1, j)
                replace = 1 + dfs(i + 1, j + 1)

                memo[(i, j)] = min(insert, delete, replace)
                return memo[(i, j)]

            else:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

        return dfs(0, 0)



word1 = "monkeys" # 2
word2 = "money"

# word1 = "neatcdee" # 3
# word2 = "neetcode"

print(Solution().minDistance(word1, word2))
        
# @lc code=end

