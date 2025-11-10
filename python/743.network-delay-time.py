from typing import List
from collections import defaultdict
import math

# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        minHeap = [(0, k)]
        heapq.heapify(minHeap)
        dist = {}
        
        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in dist:
                continue

            dist[node] = time

            for ngh, w in graph[node]:
                heapq.heappush(minHeap, (time + w, ngh))

        if len(dist) == n:
            return max(dist.values())
            
        return -1


times = [[2,1,1],[2,3,1],[3,4,1]] # 2
n = 4
k = 2

# times = [[1,2,1]] # 1
# n = 2
# k = 1

# times = [[1,2,1]] # -1
# n = 2
# k = 2


print(Solution().networkDelayTime(times, n, k))
        
# @lc code=end

