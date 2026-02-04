#
# @lc app=leetcode id=2001 lang=python3
#
# [2001] Number of Pairs of Interchangeable Rectangles
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        freq = defaultdict(int)
        res = 0

        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h //g)

            res += freq[key]
            freq[key] += 1

        return res
    
rectangles = [[4,8],[3,6],[10,20],[15,30]] # 6
print(Solution().interchangeableRectangles(rectangles))
# @lc code=end

