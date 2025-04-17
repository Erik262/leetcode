#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
            
        return nums[l]




nums = [3,4,5,1,2] # 1
# nums = [4,5,6,7,0,1,2] # 0
# nums = [11,13,15,17] # 11
# nums = [3,4,5,6,1,2] # 1


print(Solution().findMin(nums))
        
# @lc code=end

