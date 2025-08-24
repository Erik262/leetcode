from typing import List
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rest = 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += rest
                return digits
            digits[i] = 0
        return [1] + digits


digits = [1,2,3,4] # [1,2,3,5]
digits = [9,9,9] # [1,0,0,0]

print(Solution().plusOne(digits))
        
# @lc code=end

