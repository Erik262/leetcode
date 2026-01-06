#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        next_greater = {}
        stack = []
        result = []

        for x in nums2:
            while stack and x > stack[-1]:
                next_greater[stack.pop()] = x
            
            stack.append(x)

        for x in nums1:
            if x in next_greater:
                result.append(next_greater[x])
            else:
                result.append(-1)

        return result
        
# @lc code=end

