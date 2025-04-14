#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        arr = [0] * len(temperatures)
        stack = [] # temp, index

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stack_idx = stack.pop()

                arr[stack_idx] = idx - stack_idx

            stack.append([temp, idx])
        return arr

# temperatures = [30,60,90] # [1,1,0]
# temperatures = [30,40,50,60] # [1, 1, 1, 0]
# temperatures = [73,74,75,71,69,72,76,73] # [1,1,4,2,1,1,0,0]
temperatures = [55,38,53,81,61,93,97,32,43,78] # [3,1,1,2,1,1,0,1,1,0]

print(Solution().dailyTemperatures(temperatures))

# @lc code=end