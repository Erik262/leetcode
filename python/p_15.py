class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for l_idx in range(len(nums) - 2):
            l_value = nums[l_idx]
            if l_idx > 0 and l_value == nums[l_idx - 1]:
                continue
            m_idx = l_idx + 1
            r_idx = len(nums) - 1

            while m_idx < r_idx:
                diff = nums[l_idx] + nums[m_idx] + nums[r_idx] 

                if diff == 0:
                    result.append([l_value, nums[m_idx], nums[r_idx]])

                    while m_idx < r_idx and nums[m_idx] == nums[m_idx + 1]:
                        m_idx += 1

                    while m_idx < r_idx and nums[r_idx] == nums[r_idx - 1]:
                        r_idx -= 1

                    r_idx -= 1
                    m_idx += 1
                
                elif diff < 0:
                    m_idx += 1
                else:
                    r_idx -= 1                
                    
        return result

nums = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]

# nums = [0,1,1] # []

# nums = [0,0,0] # [[0,0,0]]

# nums=[-1,0,1,0] # [[-1,0,1]]
# nums=[0,0,0,0] # [[0,0,0]]

print(Solution().threeSum(nums))