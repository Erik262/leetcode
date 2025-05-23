from typing import List
from collections import deque
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = set()


        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for idx in range(len(nums)):
                if nums[idx] in used:
                    continue
                
                path.append(nums[idx])
                used.add(nums[idx])

                dfs()

                used.remove(nums[idx])
                path.pop()

        dfs()
        return res


nums = [1,2,3] # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# nums = [0,1] # [[0,1],[1,0]]

# nums = [1] # [[1]]

print(Solution().permute(nums))
        
# @lc code=end

