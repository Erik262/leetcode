#
# @lc app=leetcode id=554 lang=python3
#
# [554] Brick Wall
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)

        for row in wall:
            pos = 0

            for brick in row[:-1]:
                pos += brick
                edge_count[pos] += 1

        best_edges = max(edge_count.values(), default=0)

        return len(wall) - best_edges
    
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]] # 2
wall = [[1],[1],[1]] # 3

print(Solution().leastBricks(wall))
# @lc code=end

