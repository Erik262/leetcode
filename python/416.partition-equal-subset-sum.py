from typing import List
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        half = sum(nums) // 2
        hmap, hmap[0] = [False] * (half + 1), True

        for n in nums:
            for i in range(half, n - 1, -1):
                hmap[i] = hmap[i] or hmap[i - n]
            
        return hmap[half]

nums = [1,2,3,4] # True
# nums = [1,2,3,4,8] # True
# nums = [1,5,11,5] # True
# nums = [1,2,3,4,5] # False
# nums = [1,2,3,5] # False


print(Solution().canPartition(nums))

        
# @lc code=end

