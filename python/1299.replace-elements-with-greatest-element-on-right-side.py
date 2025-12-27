#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        rightMax = -1

        for i in range(n - 1, -1, -1):
            res[i] = rightMax

            rightMax = max(arr[i], rightMax)

        return res

# @lc code=end

