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
        half = (m + n + 1) // 2

        low, high = 0, m
        while low <= high:
            i = (low + high) // 2
            j = half - i

            if i == 0:
                max_left_1 = float("-inf")
            else:
                max_left_1 = nums1[i-1]

            if i == m:
                min_right_1 = float("inf")
            else:
                min_right_1 = nums1[i]

            if j == 0:
                max_left_2 = float("-inf")
            else:
                max_left_2 = nums2[j-1]

            if j == n:
                min_right_2 = float("inf")
            else:
                min_right_2 = nums2[j]

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                left_max = max(max_left_1, max_left_2)
                if (m + n) % 2 == 1:
                    return float(left_max)

                right_min = min(min_right_1, min_right_2)
                return (left_max + right_min) / 2.0
                
            elif max_left_1 > min_right_2:
                high = i - 1
            else:
                low = i + 1

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

