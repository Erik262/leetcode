#
# @lc app=leetcode id=1701 lang=python3
#
# [1701] Average Waiting Time
#
from typing import List
# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr_time = 0
        waiting = []

        for start, end in customers:
            if curr_time <= start:
                curr_time = start
                
            wait = abs(curr_time - start) + end
            waiting.append(wait)

            curr_time += end

        return sum(waiting) / len(customers)
# @lc code=end

