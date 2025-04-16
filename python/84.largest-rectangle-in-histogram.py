#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0 # [big,..., small (top)]

        for idx in range(len(heights)):
            if not stack:
                stack.append([idx, heights[idx]])
                continue
            
            last_pop = None
            while heights[idx] <= stack[-1][1]:
                last_pop = stack.pop()
                area = last_pop[1] * (idx - last_pop[0])
                max_area = max(area, max_area)
                if not stack:
                    break
            
            if last_pop:
                stack.append([last_pop[0], heights[idx]])
            else:
                stack.append([idx, heights[idx]])

        for idx, h in stack:
            area = h * (len(heights) - idx)
            max_area = max(max_area, area)
            
        return max_area

heights = [2,1,5,6,2,3] # 10
# heights = [2,4] # 4

# heights = [7,1,7,2,2,4] # 8
# heights = [1,3,7] # 7

print(Solution().largestRectangleArea(heights))
        
# @lc code=end

