from typing import List
import heapq
from collections import Counter
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            while heap and count[heap[0]] == 0:
                heapq.heappop(heap)

            if not heap:
                return True
            
            start = heap[0]
            need = count[start]

            for i in range(start, start + groupSize):
                if count[i] < need:
                    return False
                count[i] -= need

        return True




hand = [1,2,3,6,2,3,4,7,8] # True
groupSize = 3

# hand = [1,2,3,4,5] # False
# groupSize = 4

print(Solution().isNStraightHand(hand, groupSize))
        
# @lc code=end

