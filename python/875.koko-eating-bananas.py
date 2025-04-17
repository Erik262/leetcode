#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        hours = 0
        speed = max(piles)
        while l <= r:
            m = (l + r) // 2

            for i in range(len(piles)):
                hours += (piles[i] + m - 1) // m

            if h >= hours:
                r = m - 1
                speed = min(speed, m)
            else:
                l = m + 1
            
            hours = 0

        return speed


piles = [3,6,7,11] # 4
h = 8

# piles = [30,11,23,4,20] # 30
# h = 5

# piles = [30,11,23,4,20] # 23
# h = 6

# piles = [1,4,3,2] # 2
# h = 9


print(Solution().minEatingSpeed(piles, h))
        
# @lc code=end

