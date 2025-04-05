class Solution(object):
    def threeSum(self, nums):

        l_idx = 0
        m_idx = l_idx + 1
        r_idx = m_idx + 1
        result = []

        while l_idx < m_idx:
            l_value = nums[l_idx]
            m_value = nums[m_idx]
            r_value = nums[r_idx]

            target = l_value + m_value + r_value
            print(target)

            if target == 0:
                result.append([l_value, m_value, r_value])

            


        return result



        # s_nums = sorted(nums)

        # l_idx = 0
        # r_idx = len(s_nums) - 1
        # m_idx = l_idx + 1
        # result = []

        # while l_idx < r_idx:
        #     l_value = s_nums[l_idx]
        #     r_value = s_nums[r_idx]
        #     m_value = s_nums[m_idx]

        #     target = l_value + m_value + r_value

        #     if target == 0:
        #         if [l_value, m_value, r_value] not in result:
        #             result.append([l_value, m_value, r_value])

        #     while m_idx < r_idx:
        #         target = l_value + s_nums[m_idx] + r_value

        #         if target == 0:
        #             if [l_value, s_nums[m_idx], r_value] not in result:
        #                 result.append([l_value, s_nums[m_idx], r_value])
                
        #         m_idx += 1
                
        #     if target < 0:
        #         l_idx += 1
        #     else:
        #         r_idx -=1
            
        #     m_idx = l_idx + 1
            
        # return result






nums = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]

# nums = [0,1,1] # []

# nums = [0,0,0] # [[0,0,0]]

# nums=[-1,0,1,0] # [[-1,0,1]]

print(Solution().threeSum(nums))