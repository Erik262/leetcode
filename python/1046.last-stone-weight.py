from typing import List
import heapq
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                diff = x - y
                heapq.heappush(stones, diff)

        return abs(stones[0]) if stones else 0

stones = [2,3,6,2,4] # 1
# stones = [2,7,4,1,8,1] # 1
# stones = [1,2] # 1

print(Solution().lastStoneWeight(stones))
        
# @lc code=end

