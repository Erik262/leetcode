from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = 0

        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        def dfs(node, par):
            if node in visited:
                return
            visited.add(node)

            for neigh in adj_list[node]:
                if neigh not in visited:
                    dfs(neigh, node)

        for i in range(n):
            if i not in visited:
                comp += 1
                dfs(i, -1)

        return comp


n = 3
edges = [[0,1], [0,2]] # 1

n = 6
edges = [[0,1], [1,2], [2,3], [4,5]] # 2


print(Solution().countComponents(n, edges))