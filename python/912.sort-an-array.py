#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            arr_p, l_p, r_p = l, 0, 0 # arr_pointer, left_pointer, right_pointer

            while l_p < len(left) and r_p < len(right):
                if left[l_p] <= right[r_p]:
                    arr[arr_p] = left[l_p]
                    l_p += 1
                else:
                    arr[arr_p] = right[r_p]
                    r_p += 1

                arr_p += 1

            while l_p < len(left):
                arr[arr_p] = left[l_p]
                l_p += 1
                arr_p += 1

            while r_p < len(right):
                arr[arr_p] = right[r_p]
                r_p += 1
                arr_p += 1

        def mergesort(arr, l, r):
            if l >= r:
                return 

            m = (l+r) // 2
            mergesort(arr, l, m) # left
            mergesort(arr, m+1, r) # right
            merge(arr, l, m, r)

        mergesort(nums, 0, len(nums) - 1)
        
        return nums
        
# @lc code=end

