#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#
from typing import List, Counter
# @lc code=start
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        
        for key, val in cnt.items():

            if val == 1:
                k -= 1

            if not k:
                return key
            
        return ""
        
arr = ["d","b","c","b","c","a"]
k = 2 # a

arr = ["aaa","aa","a"]
k = 1 # aaa

# arr = ["a","b","a"]
# k = 3 # ""

print(Solution().kthDistinct(arr, k))
# @lc code=end

