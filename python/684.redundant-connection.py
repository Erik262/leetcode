from typing import List
from collections import defaultdict
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(u, target, visited):
            if u == target:
                return True
            visited.add(u)

            for ngh in graph[u]:
                if ngh not in visited and dfs(ngh, target, visited):
                    return True
            return False

        for u, v in edges:
            visited = set()

            if u in graph and v in graph and dfs(u, v, visited):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)


edges = [[1,2],[1,3],[3,4],[2,4]] # [2,4]
# edges = [[1,2],[1,3],[1,4],[3,4],[4,5]] # [3,4]

print(Solution().findRedundantConnection(edges))
        
# @lc code=end