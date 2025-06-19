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
        minHeap = [(0,0)]
        heapq.heapify(minHeap)
        visited = set()
        n = len(points)
        totalcost = 0

        while n > len(visited):
            cost, p = heapq.heappop(minHeap)
            if p in visited:
                continue

            visited.add(p)
            totalcost += cost

            for v in range(n):
                if v not in visited:
                    xi,yi = points[p]
                    xj,yj = points[v]
                    d = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(minHeap, (d, v))

        return totalcost

points = [[0,0],[2,2],[3,3],[2,4],[4,2]] # 10

print(Solution().minCostConnectPoints(points))
# @lc code=end

