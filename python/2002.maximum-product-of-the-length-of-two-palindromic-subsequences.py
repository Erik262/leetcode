#
# @lc app=leetcode id=2002 lang=python3
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#

# @lc code=start
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pal = [] # (mask, length)

        for mask in range(1, 1 << n):
            subseq = []

            for i in range(n):
                if mask & (1 << i):
                    subseq.append(s[i])
            if subseq == subseq[::-1]:
                pal.append((mask, len(subseq)))

        res = 0
        for i in range(len(pal)):
            for j in range(i + 1, len(pal)):
                m1, l1 = pal[i]
                m2, l2 = pal[j]

                if m1 & m2 == 0:
                    res = max(res, l1 * l2)

        return res
    

print(3 << 1) # 0011 -> 0110 = 6
print(1 << 3) # 0001 -> 1000 = 8 or 2^3

s = "leetcodecom"
print(Solution().maxProduct(s))
        
# @lc code=end

