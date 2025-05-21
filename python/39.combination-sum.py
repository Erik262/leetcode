from typing import List
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp_val = []

        def dfs(idx: int, tmp_val: List[int], tot_val: int):
            if tot_val == target:
                res.append(tmp_val.copy())
                return
            
            if tot_val > target or idx >= len(candidates):
                return
            
            tmp_val.append(candidates[idx])
            dfs(idx, tmp_val, tot_val + candidates[idx])
            
            tmp_val.pop()
            dfs(idx + 1, tmp_val, tot_val)

        dfs(0, tmp_val, 0)

        return res



candidates = [2,5,6,9] # [[2,2,5],[9]]
target = 9

# candidates = [2,3,6,7] # [[2,2,3],[7]]
# target = 7

# candidates = [2,3,5] # [[2,2,2,2],[2,3,3],[3,5]]
# target = 8

# candidates = [2] # []
# target = 1

print(Solution().combinationSum(candidates, target))
        
# @lc code=end

