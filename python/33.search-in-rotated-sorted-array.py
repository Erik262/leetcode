#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot = 0

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            pivot = l
            
        if nums[pivot] <= target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
                

nums = [4,5,6,7,0,1,2] # 4
target = 0

# nums = [4,5,6,7,0,1,2] # -1
# target = 3

# nums = [1] # -1
# target = 0

# nums = [1,3] # 1
# target = 3

# nums = [4,0,1,2,3]
# target = 0

print(Solution().search(nums, target))
        
# @lc code=end

