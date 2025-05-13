from typing import List
import heapq
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

        while len(self.heap) > k:
            heapq.heappop(self.heap)
            
    
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
       
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [1, 2, 3, 3])
obj.add(3) # 3
obj.add(5) # 3
obj.add(6) # 3
obj.add(7) # 5
obj.add(8) # 6

# @lc code=end

