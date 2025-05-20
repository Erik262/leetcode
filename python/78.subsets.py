from typing import List
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub = []

        def dfs(index):
            if index >= len(nums):
                result.append(sub.copy())
                return

            sub.append(nums[index])

            dfs(index + 1)
            
            sub.pop()
            dfs(index + 1)

        dfs(0)
        return result



nums = [1,2,3] # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# nums = [7] # [[],[7]]

print(Solution().subsets(nums))
        
# @lc code=end