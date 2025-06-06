#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(my_node: Optional['Node']):
            if my_node in cloned:
                return cloned[my_node]
            
            if not my_node:
                return None
            
            cloned_node = Node()
            cloned_node.val = my_node.val
            cloned[my_node] = cloned_node

            for n in my_node.neighbors:
                cloned_node.neighbors.append(dfs(n))


            return cloned_node
        
        # print(cloned)
        return dfs(node)

            







def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]

    return nodes[0] 


from collections import deque

def graph_to_adjlist(node):
    if not node:
        return []

    visited = {}
    queue = deque([node])

    while queue:
        current = queue.popleft()
        if current.val in visited:
            continue

        visited[current.val] = [neighbor.val for neighbor in current.neighbors]

        for neighbor in current.neighbors:
            if neighbor.val not in visited:
                queue.append(neighbor)

    max_val = max(visited.keys())
    adj_list = [[] for _ in range(max_val)]
    for k in visited:
        adj_list[k - 1] = visited[k]

    return adj_list

adjList = [[2],[1,3],[2]] # [[2],[1,3],[2]]
# adjList = [[]] # [[]]

start_node = build_graph(adjList)
cloned_node = Solution().cloneGraph(start_node)
print(graph_to_adjlist(cloned_node))

# @lc code=end

