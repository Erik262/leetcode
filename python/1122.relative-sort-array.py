#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
#
from typing import List, Counter
# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt = Counter(arr1)
        res = []

        for x in arr2:
            res.extend([x] * cnt[x])
            del cnt[x]

        for x in sorted(cnt):
            res.extend([x] * cnt[x])

        return res
    

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6] # [2,2,2,1,4,3,3,9,6,7,19]

print(Solution().relativeSortArray(arr1, arr2))
# @lc code=end

