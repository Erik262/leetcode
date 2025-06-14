from typing import List
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parrent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n):
            if n != parrent[n]:
                parrent[n] = find(parrent[n])
            return parrent[n]
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parrent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parrent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        



edges = [[1,2],[1,3],[3,4],[2,4]] # [2,4]
# edges = [[1,2],[1,3],[1,4],[3,4],[4,5]] # [3,4]

print(Solution().findRedundantConnection(edges))
        
# @lc code=end

