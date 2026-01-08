#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
from typing import List
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []

        for i in range(len(nums) + 1):
            self.prefixSum.append(sum(nums[:i]))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right + 1] - self.prefixSum[left]


arr = [-2,0,3,-5,2,-1]
foo = NumArray(arr)
print(foo.sumRange(0,5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

