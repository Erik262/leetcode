#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        i = 0
        if n == 0:
            return True
            
        while i < m:
            if flowerbed[i] == 0:
                left_ok = (i == 0) or (flowerbed[i - 1] == 0)
                right_ok = (i == m - 1) or (flowerbed[i + 1] == 0)

                if left_ok and right_ok:
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
                    i += 2
                    continue

            i += 1

        return n == 0


        
flowerbed = [1,0,0,0,1]
n = 2 # False

# flowerbed = [1,0,1,0,1,0,1]
# n = 1 # False

flowerbed = [0,0,1,0,0]
n = 2 # True

print(Solution().canPlaceFlowers(flowerbed, n))
# @lc code=end

