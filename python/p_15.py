class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []

        for l_idx in range(n-2):
            m_idx, r_idx = l_idx+1, n-1
            if l_idx > 0 and nums[l_idx] == nums[l_idx-1]:
                continue

            while m_idx < r_idx:
                target = nums[l_idx] + nums[m_idx] + nums[r_idx]

                if target == 0:
                    result.append([nums[l_idx], nums[m_idx], nums[r_idx]])
                    
                    while m_idx < r_idx and nums[m_idx] == nums[m_idx+1]:
                        m_idx += 1

                    while m_idx < r_idx and nums[r_idx] == nums[r_idx-1]:
                        r_idx -= 1

                    m_idx += 1
                    r_idx -= 1

                if target < 0:
                    m_idx += 1
                
                if target > 0:
                    r_idx -= 1

        return result

nums = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]

# nums = [0,1,1] # []
# nums = [0,0,0] # [[0,0,0]]
# nums=[-1,0,1,0] # [[-1,0,1]]
# nums=[0,0,0,0] # [[0,0,0]]

print(Solution().threeSum(nums))