from typing import List
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        start = 0
        tank = 0
        total = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            tank += diff
            total += tank

            if tank < 0:
                start = i + 1
                tank = 0

        if total >= 0:
            return start
        else:
            return -1


gas = [1,2,3,4] # 3
cost = [2,2,4,1]

gas = [1,2,3,4,5] # 3
cost = [3,4,5,1,2]

# gas = [1,2,3] # -1
# cost = [2,3,2]

print(Solution().canCompleteCircuit(gas, cost))
        
# @lc code=end