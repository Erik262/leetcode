from typing import List
from collections import defaultdict
import math
import heapq
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        hmap = {i: [] for i in range(n)}
        minHeap = [(0, src, 0)]
        heapq.heapify(minHeap)
        visited = {}

        for s, d, c in flights:
            hmap[s].append([d, c])

        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)

            if node == dst:
                return cost
            
            if stops > k:
                continue
            
            for nigh, cst in hmap[node]:
                n_cost = cost + cst
                key = (nigh, stops + 1)
                if key not in visited or visited[key] > n_cost:
                    visited[key] = n_cost
                    heapq.heappush(minHeap, (n_cost, nigh, stops + 1))

        return -1


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
# 700

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
# 200

# n = 3
# flights = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 0
# 500

# n=5
# flights=[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
# src=2
# dst=1
# k=1
# -1

print(Solution().findCheapestPrice(n, flights, src, dst, k))

# @lc code=end

