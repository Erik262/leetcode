from typing import List
from collections import defaultdict
import math
import heapq

# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)] # (cost, node)
        res = 0
        heapq.heapify(min_heap)

        while len(visited) < n:
            cost, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            res += cost

            x1, y1 = points[node]
            for ngh in range(n):
                if ngh not in visited:
                    x2, y2 = points[ngh]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (dist, ngh))

        return res

points = [[0,0],[2,2],[3,3],[2,4],[4,2]] # 10

print(Solution().minCostConnectPoints(points))
# @lc code=end

