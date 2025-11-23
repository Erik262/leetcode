from typing import List
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(idx: int, tmp_list: List[int], tot_val: int):
            if tot_val == target:
                result.append(tmp_list.copy())
                return
            
            if tot_val > target:
                return

            if idx >= len(candidates) or tot_val > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                tmp_list.append(candidates[i])
                dfs(i + 1, tmp_list, tot_val + candidates[i])
                tmp_list.pop()

        dfs(0, [], 0)
        return result 


candidates = [9,2,2,4,6,1,5] # [[1,2,5], [2,2,4], [2,6]]
target = 8

# candidates = [1,2,3,4,5] # [[1,2,4], [2,5], [3,4]]
# target = 7


print(Solution().combinationSum2(candidates, target))
# @lc code=end