#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        unbalanced = 0

        for ch in s:
            if ch == '[':
                balance += 1
            elif ch == ']' and balance > 0:
                balance -= 1
            elif ch == ']' and balance == 0:
                unbalanced += 1

        return (unbalanced + 1) // 2
# @lc code=end

