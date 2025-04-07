class Solution(object):
    def trap(self, height):

        l_idx = 0
        r_idx = len(height) - 1
        liter = 0
        l_max = 0
        r_max = 0

        while l_idx < r_idx:
            if height[l_idx] < height[r_idx]:
                if height[l_idx] < l_max:
                    liter += l_max - height[l_idx]
                else:
                    l_max = height[l_idx]
                l_idx += 1
            else:
                if height[r_idx] < r_max:
                    liter += r_max - height[r_idx]
                else:
                    r_max = height[r_idx]
                r_idx -= 1

        return liter


height = [0,2,0,3,1,0,1,3,2,1] # 9
# height = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
# height = [4,2,0,3,2,5] # 9
print(Solution().trap(height))