from typing import List
from collections import deque
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1. Add all rotten oranges to queue, count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))   # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh += 1
        
        # Step 2. BFS
        minutes = 0
        while queue:
            r, c, t = queue.popleft()
            minutes = max(minutes, t)          # keep track of last minute
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
        
        # Step 3. If fresh oranges remain, return -1
        return minutes if fresh == 0 else -1


grid = [[2,1,1],[1,1,0],[0,1,1]] # 4
# grid = [[2,1,1],[0,1,1],[1,0,1]] # -1
# grid = [[0,2]] # 0

print(Solution().orangesRotting(grid))
        
# @lc code=end

