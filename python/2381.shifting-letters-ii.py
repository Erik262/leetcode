#
# @lc app=leetcode id=2381 lang=python3
#
# [2381] Shifting Letters II
#
from typing import List
# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for l, r, direction in shifts:
            delta = 1 if direction == 1 else -1
            diff[l] += delta
            if r + 1 < n:
                diff[r+1] -= delta

        res = []
        running = 0
        for i, ch in enumerate(s):
            running += diff[i]
            x = (ord(ch) - ord('a') + running) % 26
            res.append(chr(x + ord('a')))

        return ''.join(res)
    
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

print(Solution().shiftingLetters(s, shifts))
        
# @lc code=end

