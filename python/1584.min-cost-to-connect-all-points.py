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
        in_mst = [False] * n
        min_dist = [float('inf')] * n
        min_dist[0] = 0
        cost = 0
        
        for _ in range(n):
            u = -1
            min_cost = float('inf')
            for i in range(n):
                if not in_mst[i] and min_dist[i] < min_cost:
                    min_cost = min_dist[i]
                    u = i

            in_mst[u] = True
            cost += min_dist[u]

            for v in range(n):
                if not in_mst[v]:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    if dist < min_dist[v]:
                        min_dist[v] = dist

        return cost

points = [[0,0],[2,2],[3,3],[2,4],[4,2]] # 10

print(Solution().minCostConnectPoints(points))
# @lc code=end

