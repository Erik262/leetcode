#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_arr1 = set()
        best = 0

        for n1 in arr1:
            pre = ""

            for ch in str(n1):
                pre += ch
                prefix_arr1.add(pre)

        for n2 in arr2:
            n2_str = str(n2)

            for i in range(len(n2_str)):
                num = n2_str[:len(n2_str) - i]

                if num in prefix_arr1:
                    best = max(best, len(num))
                    break

        return best
# @lc code=end

