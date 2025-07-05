#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            curr_i = 0
            for j in range(len(text2) - 1, -1, -1):
                curr_j = dp[j]

                if text1[i] == text2[j]:
                    dp[j] = 1 + curr_i
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                
                curr_i = curr_j

        return dp[0]
    
text1 = "cat" # 3
text2 = "crabt" 

text1 = "abcd" # 4
text2 = "abcd"

text1 = "abcd" # 0
text2 = "efgh"

print(Solution().longestCommonSubsequence(text1, text2))
        
# @lc code=end

