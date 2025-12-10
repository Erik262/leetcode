import heapq
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

        heapq.heapify(self.maxHeap)
        heapq.heapify(self.minHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        
        elif len(self.minHeap) > len(self.maxHeap):
            return float(self.minHeap[0])
        
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

            



# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]

# Output
# [null, null, null, 1.5, null, 2.0]

medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.findMedian()
# medianFinder.addNum(2)    # arr = [1, 2]
# medianFinder.findMedian()
# medianFinder.addNum(3)    # arr = [1, 2]
# medianFinder.findMedian()
# medianFinder.addNum(4)    # arr = [1, 2]
# medianFinder.addNum(5)    # arr = [1, 2]
# medianFinder.addNum(6)    # arr = [1, 2]
# medianFinder.addNum(7)    # arr = [1, 2]
# medianFinder.findMedian() # return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3)    # arr[1, 2, 3]
# medianFinder.findMedian() # return 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

