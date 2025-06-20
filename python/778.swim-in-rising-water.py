from typing import List
import heapq
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]] # level, row, col
        visited = set()
        visited.add((0,0))
        direction = [[0,1], [1,0], [-1,0], [0,-1]] # right, down, up, left

        while minHeap:
            lv, r, c = heapq.heappop(minHeap)
            if (r == n - 1) and (c == n - 1):
                return lv
            
            for d_row, d_col in direction:
                neigh_r, neigh_c = r + d_row, c + d_col # compute next position

                # check if in grid range
                if neigh_r < 0 or neigh_r >= n or neigh_c < 0 or neigh_c >= n or (neigh_r, neigh_c) in visited:
                    continue

                visited.add((neigh_r, neigh_c))
                heapq.heappush(minHeap, [max(lv, grid[neigh_r][neigh_c]), neigh_r, neigh_c])


grid = [[0,1],[2,3]] # 3

grid = [
  [0,1,2,10],
  [9,14,4,13],
  [12,3,8,15],
  [11,5,7,6]]
# 8

print(Solution().swimInWater(grid))
# @lc code=end

