#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n) // 2

        l, r = 0, m - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            left1 = nums1[i] if i >= 0 else float("-inf")
            right1 = nums1[i+1] if i + 1 < m else float("inf")
            left2 = nums2[j] if j >= 0 else float("-inf")
            right2 = nums2[j+1] if j + 1 < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return float(min(right1, right2))

                left_max = max(left1, left2)
                right_min = min(right1, right2)
                
                return (left_max + right_min) / 2.0

            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1

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

