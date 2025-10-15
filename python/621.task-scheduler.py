from typing import List
import heapq
from collections import Counter
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        max_heap = [-x for x in counter.values()]
        heapq.heapify(max_heap)

        queue = []
        timer = 0

        while max_heap or queue:
            timer += 1

            if max_heap:
                remain = 1 + heapq.heappop(max_heap)
                if remain:
                    queue.append([remain, timer + n])
            
            if queue and queue[0][1] == timer:
                heapq.heappush(max_heap, queue.pop(0)[0])

        return timer



tasks = ["A","A","A","B","B","B"] # 8
n = 2

tasks = ["A","C","A","B","D","B"] # 6
n = 1

# tasks = ["A","A","A", "B","B","B"] # 10
# n = 3

print(Solution().leastInterval(tasks, n))
        
# @lc code=end

