from typing import List
import math
import heapq
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []

        def eucl(points: List) -> float:
            return -((0 - points[0])**2 + (0 - points[1])**2)
        
        for p in points:
            result.append([eucl(p), p])

        heapq.heapify(result)
        res = []

        while len(result) > k:
            heapq.heappop(result)

        result = [p for dist, p in result]
        return result

points = [[1,3],[-2,2]] # [[-2,2]]
k = 1

points = [[3,3],[5,-1],[-2,4]] # [[3,3],[-2,4]]
k = 2

points = [[1,3],[-2,2],[2,-2]] # [[-2,2],[2,-2]]
k = 2

print(Solution().kClosest(points, k))
        
# @lc code=end

