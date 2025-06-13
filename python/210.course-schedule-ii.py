from typing import List
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}
        visited = set()
        visiting =set()
        res = []

        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return True
            
            if crs in visiting:
                return False

            visiting.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
                
            visiting.remove(crs)
            visited.add(crs)

            pre_map[crs] = []
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res

numCourses = 3
prerequisites = [[1,0]] # [0,1,2]

numCourses = 2
prerequisites = [[0,1]] # [1,0]

# numCourses = 3
# prerequisites = [[0,1],[1,2],[2,0]] # []

print(Solution().findOrder(numCourses, prerequisites))
        
# @lc code=end

