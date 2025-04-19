#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        mid = n // 2
        if n % 2:
            return merged[mid]
        return (merged[mid - 1] + merged[mid]) / 2

nums1 = [123, 2459, 789] # 270
nums2 = [240, 300, 13]

# nums1 = [0,0]
# nums2 = [0,0]

# nums1 = [1,2] # 2.50000
# nums2 = [4,3]

# nums1 = [1,3] # 2.00000
# nums2 = [2]

# odd (n + 1)/2
# even ((n/2) + ((n/2) + 1))/2

# nums1 = [1,3] # 2.00000
# nums2 = [2]

# nums1 = [1,2] # 2.50000
# nums2 = [3,4]


print(Solution().findMedianSortedArrays(nums1, nums2))
        
# @lc code=end

