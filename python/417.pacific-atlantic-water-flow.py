from typing import List
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        visited = set()

        def dfs(i: int, j: int, visited: set, prevH: int):

            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in visited or heights[i][j] < prevH:
                return
            
            visited.add((i,j))

            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

            for col in range(cols):
                dfs(0, col, pacific, heights[0][col])
                dfs(rows - 1, col, atlantic, heights[rows - 1][col])

            for row in range(rows):
                dfs(row, 0, pacific, heights[row][0])
                dfs(row, cols - 1, atlantic, heights[row][cols - 1])

            result = []
            for r in range(rows):
                for c in range(cols):
                    if (r,c) in pacific and (r,c) in atlantic:
                        result.append([r,c])
                
            return result
        return dfs(0, 0, visited, 0)

            



heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# heights = [[1]]
# [[0,0]]

print(Solution().pacificAtlantic(heights))
# @lc code=end

