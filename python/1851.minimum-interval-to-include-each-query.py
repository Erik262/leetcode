from typing import List
import heapq
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q_pair = sorted(enumerate(queries), key=lambda x: x[1]) # (idx, val)
        minHeap = []
        heapq.heapify(minHeap)
        result = [-1] * len(queries)
        pos = 0

        for idx, qv in q_pair:
            print(idx, qv)
            while pos < len(intervals) and intervals[pos][0] <= qv:
                l, r, = intervals[pos][0], intervals[pos][1]
                heapq.heappush(minHeap, (r - l + 1, r))

                pos += 1

            while minHeap and minHeap[0][1] < qv:
                heapq.heappop(minHeap)

            if minHeap:
                result[idx] = minHeap[0][0]
            
        return result


intervals = [[1,3],[2,3],[3,7],[6,6]] # [2,2,3,5,1,-1]
queries = [2,3,1,7,6,8]

# intervals = [[1,4],[2,4],[3,6],[4,4]] # [3,3,1,4]
# queries = [2,3,4,5]

# intervals = [[2,3],[2,5],[1,8],[20,25]] # [2,-1,4,6]
# queries = [2,19,5,22]

print(Solution().minInterval(intervals, queries))
        
# @lc code=end

