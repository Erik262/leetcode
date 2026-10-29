#
# @lc app=leetcode id=2570 lang=python3
#
# [2570] Merge Two 2D Arrays by Summing Values
#
from typing import List
# @lc code=start
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        m, n = len(nums1), len(nums2)

        l, r = 0, 0

        while l < m and r < n:
            if nums1[l][0] == nums2[r][0]:
                idx = nums1[l][0]
                val = nums1[l][1] + nums2[r][1]
                result.append([idx, val])

                l += 1
                r += 1

            else:
                if nums1[l][0] < nums2[r][0]:
                    result.append(nums1[l])
                    l += 1

                else:
                    result.append(nums2[r])
                    r += 1

        if len(nums1[l:]) > 0: result.extend(nums1[l:])
        if len(nums2[r:]) > 0: result.extend(nums2[r:])

        return result
# @lc code=end

