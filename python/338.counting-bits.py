from typing import List
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            # print(f"i: {i}, result[i >> 1]: {result[i >> 1]}, (i & 1): {(i & 1)} --> {result[i >> 1] + (i & 1)}")
            result[i] = result[i >> 1] + (i & 1)

        return result
    

n = 4 # [0,1,1,2,1]

print(Solution().countBits(n))

        
# @lc code=end

