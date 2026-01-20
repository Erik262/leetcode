#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#
from typing import List
# @lc code=start
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0

        while tickets[k] != 0:
            for t in range(len(tickets)):
                print(tickets)
                if tickets[k] == 0:
                    return cnt
                
                if tickets[t] == 0:
                    continue
                
                tickets[t] -= 1
                cnt += 1
            
        return cnt
        
tickets = [2,3,2]
k = 2 # 6
print(Solution().timeRequiredToBuy(tickets, k))
# @lc code=end

