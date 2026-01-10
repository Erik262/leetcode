#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#
from typing import List, Counter
# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)

        for a, b in cnt.most_common():
            if a == b:
                return a

        return -1

arr = [1,2,2,3,3,3] # 3
print(Solution().findLucky(arr))
# @lc code=end

