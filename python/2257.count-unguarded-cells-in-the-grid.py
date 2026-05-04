#
# @lc app=leetcode id=2257 lang=python3
#
# [2257] Count Unguarded Cells in the Grid
#
from typing import List
# @lc code=start
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guard_set = set(map(tuple, guards))
        wall_set = set(map(tuple, walls))
        seen = set()

        for r, c in guards:

            # left
            col = c - 1
            while col >= 0:
                if (r, col) in guard_set or (r, col) in wall_set:
                    break

                seen.add((r, col))
                col -= 1

            # right
            col = c + 1
            while col < n:
                if (r, col) in guard_set or (r, col) in wall_set:
                    break

                seen.add((r, col))
                col += 1

            # up
            row = r - 1
            while row >= 0:
                if (row, c) in guard_set or (row, c) in wall_set:
                    break
                
                seen.add((row, c))
                row -= 1

            # down
            row = r + 1
            while row < m:
                if (row, c) in guard_set or (row, c) in wall_set:
                    break

                seen.add((row, c))
                row += 1

        return m * n - len(guards) - len(walls) - len(seen)


m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]
# 7

print(Solution().countUnguarded(m, n, guards, walls))
# @lc code=end

