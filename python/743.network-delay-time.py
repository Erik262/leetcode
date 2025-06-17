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
        hmap = defaultdict(list)
        dmap = {i: math.inf for i in range(1, n + 1)}

        for u, v, t in times:
            hmap[u].append((v, t))

        def dfs(snode, time):
            if time >= dmap[snode]:
                return

            dmap[snode] = time
            for v, t in hmap[snode]:
                dfs(v, time + t)

        dfs(k, 0)
        result = max(dmap.values())

        if result < math.inf:
            return result
        else:
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

