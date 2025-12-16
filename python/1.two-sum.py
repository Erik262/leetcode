class Solution(object):
    def twoSum(self, nums, target):
        h_map = {}

        for idx, item in enumerate(nums):
            diff = target - item

            if diff in h_map:
                return [h_map[diff], idx]
            
            h_map[item] = idx

nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums,target))