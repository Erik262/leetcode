#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        first = []
        open_count = 0

        for ch in s:
            if ch == '(':
                open_count += 1
                first.append(ch)

            elif ch == ')':
                if open_count > 0:
                    open_count -= 1
                    first.append(ch)
            else:
                first.append(ch)

        result = []
        for ch in reversed(first):
            if ch == '(' and open_count > 0:
                open_count -= 1
            else:
                result.append(ch)

        return ''.join(reversed(result))
# @lc code=end

