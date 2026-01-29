#
# @lc app=leetcode id=2780 lang=python3
#
# [2780] Minimum Index of a Valid Split
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        d_elm, d_occ = cnt.most_common()[0]
        n = len(nums)

        left_cnt = 0
        for i in range(n - 1):
            if nums[i] == d_elm:
                left_cnt += 1

            left_len = i + 1
            right_len = n - left_len
            right_cnt = d_occ - left_cnt

            if left_cnt * 2 > left_len and right_cnt * 2 > right_len:
                return i
            
        return -1


nums = [2,1,3,1,1,1,7,1,2,1] # 4
# nums = [1,2,2,2] # 2
print(Solution().minimumIndex(nums))
# @lc code=end