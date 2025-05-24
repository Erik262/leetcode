from typing import List
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(start):
            res.append(path.copy())

            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue

                path.append(nums[idx])

                dfs(idx + 1)

                path.pop()

        dfs(0)
        return res

nums = [1,2,2] # [[],[1],[1,2],[1,2,2],[2],[2,2]]
# nums = [0] # [[],[0]]



print(Solution().subsetsWithDup(nums))
# @lc code=end