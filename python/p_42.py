class Solution(object):
    def trap(self, height):

        l_idx = 0
        r_idx = l_idx + 1
        liter = 0
        tmp_liter = 0
        u = height[0] > height[1] 

        while r_idx < len(height):
            if u:
                if height[l_idx] < height[r_idx]:
                    # tmp_liter += (height[r_idx] - height[l_idx])
                    tmp_liter = min(height[r_idx], height[l_idx])
                    print(tmp_liter)
                    l_idx = r_idx
                    r_idx += 1

                if height[l_idx] == height[r_idx]:
                    liter = tmp_liter
                    tmp_liter = 0
                    # l_idx = r_idx
                    # r_idx = l_idx + 1
                    u = False

                if height[l_idx] > height[r_idx]:
                    tmp_liter += (height[l_idx] - height[r_idx])
                    # tmp_liter = min(height[l_idx], height[r_idx])
                    r_idx += 1

            else:
                l_idx = r_idx
                r_idx += 1
                if height[l_idx] > height[r_idx]:
                    u = True



        
        return liter







        


height = [0,2,0,3,1,0,1,3,2,1] # 9
# height = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
# height = [4,2,0,3,2,5] # 9
print(Solution().trap(height))