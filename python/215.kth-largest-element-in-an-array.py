from typing import List
import heapq
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while k < len(nums):
            heapq.heappop(nums)

        return nums[0]

nums = [3,2,1,5,6,4] # 5
k = 2

# nums = [3,2,3,1,2,4,5,5,6] # 4
# k = 4

print(Solution().findKthLargest(nums, k))

# @lc code=end

