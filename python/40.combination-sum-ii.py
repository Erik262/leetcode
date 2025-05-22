from typing import List
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp_val = []
        candidates.sort()

        def dfs(idx: int, tmp_val: List[int], total: int):
            if total == target:
                res.append(tmp_val.copy())
                return
            
            if total > target or idx >= len(candidates):
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                tmp_val.append(candidates[i])
                dfs(i + 1, tmp_val, total + candidates[i])
                tmp_val.pop()

        dfs(0, tmp_val, 0)
        return res


candidates = [9,2,2,4,6,1,5] # [[1,2,5], [2,2,4], [2,6]]
target = 8

# candidates = [1,2,3,4,5] # [[1,2,4], [2,5], [3,4]]
# target = 7


print(Solution().combinationSum2(candidates, target))
# @lc code=end