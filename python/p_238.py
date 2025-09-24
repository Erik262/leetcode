class Solution(object):
    def productExceptSelf(self, nums):
        
        arr = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            arr[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            arr[i] *= postfix
            postfix *= nums[i]

        return arr

nums = [1,2,3,4]
nums2 = [-1,1,0,-3,3]

print(Solution().productExceptSelf(nums))