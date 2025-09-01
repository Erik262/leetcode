from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        
        # undirected adjacency list
        adj_list = [[] for i in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node, par):
            visited.add(node)

            for neigh in adj_list[node]:
                if neigh == par:
                    continue

                if neigh in visited:
                    return False

                if not dfs(neigh, node):
                    return False
                
            return True
        
        return dfs(0, -1) and len(visited) == n

n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]] # True

n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]] # False

n = 4
edges = [[0,1],[2,3],[1,2]] # True


print(Solution().validTree(n, edges))