from typing import List
from collections import defaultdict, deque
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        taken_courses = 0
        while queue:
            course = queue.popleft()
            taken_courses += 1

            for ngh in graph[course]:
                in_degree[ngh] -= 1

                if in_degree[ngh] == 0:
                    queue.append(ngh)
        
        return taken_courses == numCourses



numCourses = 2
prerequisites = [[0,1]] # True


# numCourses = 2
# prerequisites = [[0,1],[1,0]] # False
        

print(Solution().canFinish(numCourses, prerequisites))

# @lc code=end

