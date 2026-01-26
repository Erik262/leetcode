#
# @lc app=leetcode id=1769 lang=python3
#
# [1769] Minimum Number of Operations to Move All Balls to Each Box
#
from typing import List
# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        take = 0
        balls = 0
        for i in range(n):
            result[i] += take
            if boxes[i] == '1':
                balls += 1
            take += balls

        take = 0
        balls = 0
        for j in range(n - 1, -1, -1):
            result[j] += take
            if boxes[j] == '1':
                balls += 1
            take += balls

        return result
    
boxes = "001011"
boxes = "110"
print(Solution().minOperations(boxes))
# @lc code=end

