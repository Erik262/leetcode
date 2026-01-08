#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
from typing import List
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = list(range(1, len(nums) + 1))

        for n in nums:
            if n in result:
                result.remove(n)

        return result
    

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))

# @lc code=end

