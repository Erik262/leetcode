#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        answer = [list(s1 - s2), list(s2 - s1)]

        return answer

nums1 = [1,2,3]
nums2 = [2,4,6]

print(Solution().findDifference(nums1, nums2))
# @lc code=end

