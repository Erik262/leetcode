class Solution(object):
    def containsDuplicate(self, nums):
        hmap = set()

        for num in nums:
            if num in hmap:
                return True

            hmap.add(num)
            
        return False

nums = [1,2,3,0]

print(Solution().containsDuplicate(nums))