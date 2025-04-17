#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            n = nums[m]
            if target > n:
                l = m + 1
            elif target < n:
                r = m - 1
            else:
                return m
            
        return -1


nums = [-1,0,2,4,6,8] # 3
target = 4

# nums = [-1,0,3,5,9,12] # 4
# target = 9

# nums = [-1,0,3,5,9,12] # -1
# target = 2

print(Solution().search(nums, target))

# @lc code=end

