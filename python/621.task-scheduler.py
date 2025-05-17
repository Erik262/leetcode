from typing import List
import heapq
from collections import Counter, deque
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cnt = Counter(tasks)
        heap = [-x for x in cnt.values()]
        heapq.heapify(heap)

        queue = deque()
        timer = 0

        while heap or queue:
            timer += 1

            if heap:
                count = 1 + heapq.heappop(heap)
                if count:
                    queue.append([count, timer + n])

            if queue and queue[0][1] == timer:
                heapq.heappush(heap, queue.popleft()[0])


        return timer



tasks = ["A","A","A","B","B","B"] # 8
n = 2

tasks = ["A","C","A","B","D","B"] # 6
n = 1

# tasks = ["A","A","A", "B","B","B"] # 10
# n = 3

print(Solution().leastInterval(tasks, n))
        
# @lc code=end

