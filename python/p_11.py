class Solution(object):
    def maxArea(self, height):

        liter = 0
        l_idx = 0
        r_idx = len(height) - 1

        while l_idx < r_idx:
            l_v = height[l_idx]
            r_v = height[r_idx]

            tmp_liter = min(height[l_idx], height[r_idx]) * (r_idx - l_idx)
            liter = max(liter, tmp_liter)

            if l_v < r_v:
                l_idx += 1
            else:
                r_idx -= 1

        return liter

height = [1,7,2,5,4,7,3,6] # 36
# height = [2,2,2] # 4
# height = [1,8,6,2,5,4,8,3,7] # 49
print(Solution().maxArea(height))