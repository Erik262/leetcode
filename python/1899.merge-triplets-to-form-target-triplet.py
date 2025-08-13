from typing import List
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hitX, hitY, hitZ = False, False, False

        for arr in triplets:
            if arr[0] <= target[0] and arr[1] <= target[1] and arr[2] <= target[2]:

                hitX |= arr[0] == target[0]
                hitY |= arr[1] == target[1]
                hitZ |= arr[2] == target[2]

        return hitX and hitY and hitZ

triplets = [[1,2,3],[7,1,1]] # True
target = [7,2,3]

triplets = [[2,5,6],[1,4,4],[5,7,5]] # False
target = [5,4,6]

print(Solution().mergeTriplets(triplets, target))
        
# @lc code=end

