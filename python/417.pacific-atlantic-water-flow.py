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

        def dfs(row, col, prev, ocean):
            if (row, col) in ocean:
                return

            if not (0 <= row < rows and 0 <= col < cols):
                return
            
            if prev > heights[row][col]:
                return

            ocean.add((row, col))
            dfs(row, col + 1, heights[row][col], ocean) # right
            dfs(row + 1, col, heights[row][col], ocean) # down
            dfs(row, col - 1, heights[row][col], ocean) # left
            dfs(row - 1, col, heights[row][col], ocean) # up

        for row in range(rows):
            dfs(row, 0, 0, pacific)
            dfs(row, cols - 1, 0, atlantic)
        
        for col in range(cols):
            dfs(0, col, 0, pacific)
            dfs(rows - 1, col, 0, atlantic)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
                    
        return result

            



heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

# heights = [[1]]
# [[0,0]]

print(Solution().pacificAtlantic(heights))
# @lc code=end

